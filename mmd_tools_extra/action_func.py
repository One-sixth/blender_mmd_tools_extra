from math import inf
import bpy
import time
from .misc import alert_msg, filter_mmd_joint, filter_mmd_rigidbody
from .simple_progressbar import update_progress, finish_progress


def disable_constraints(obj):
    # 关闭对象的约束，并返回对象之前的约束状态
    ctr_state = []
    for ctr in obj.constraints:
        ctr_state.append(ctr.enabled)
        ctr.enabled = False
    return ctr_state


def recover_constraints(obj, ctr_state):
    # 根据约束状态，恢复对象的约束
    for ctr, state in zip(obj.constraints, ctr_state):
        ctr.enabled = state


def disable_all_constraints(objs):
    ctr_states = {}
    for obj in objs:
        ctr_state = disable_constraints(obj)
        ctr_states[obj.name] = ctr_state
    return ctr_states


def recover_all_constraints(objs, ctr_states):
    for obj in objs:
        for ctr, state in zip(obj.constraints, ctr_states[obj.name]):
            ctr.enabled = state


def get_or_create_fcurve(action, bone_name, channel_i, axis_i, data_path):
    if bone_name not in action.groups:
        g = action.groups.new(bone_name)
    g = action.groups[bone_name]
    
    # 如果已有的通道数量不够，就新增空的通道，直到通道数量满足需要
    while channel_i >= len(g.channels):
        action.fcurves.new('none', index=0, action_group=bone_name)

    # 获得指定通道
    fc = g.channels[channel_i]
    # 如果通道的数据路径不对，直接替换掉原来的
    # TODO 这里写成判断是为了在未来增加警告信息输出，目前没写
    if fc.data_path != data_path:
        fc.data_path = data_path
    if fc.array_index != axis_i:
        fc.array_index = axis_i
    
    return fc


def clean_fcurve(all_bone_fcurves, eps=1e-4, max_clean_cycle=-1):
    # 本步中，关键帧必须是按时间顺序排列的，否则可能会发生意外
    # modify from Blender/3.2/scripts/modules/bpy_extras/anim_utils.py

    # clean_orig_data = {fcu: {p.co[1] for p in fcu.keyframe_points} for fcu in action.fcurves}

    if max_clean_cycle <= 0:
        max_clean_cycle = inf

    for fcu_i, fcu in enumerate(all_bone_fcurves):
        update_progress(f'Cleaning bone curves.', (fcu_i+1)/len(all_bone_fcurves))
        
        # 自动排序关键帧，确保关键帧按时间顺序排列，这在clean时非常重要
        fcu.update()

        # fcu_orig_data = clean_orig_data.get(fcu, set())

        # 加入循环清理
        need_next_clean_cycle = True
        cur_clean_cycle = 0
        # 成功清理计数
        del_count = 0

        while need_next_clean_cycle and cur_clean_cycle < max_clean_cycle:
            cur_clean_cycle += 1
            need_next_clean_cycle = False

            keyframe_points = fcu.keyframe_points
            i = 1

            while i < len(keyframe_points) - 1:
                val = keyframe_points[i].co[1]
                frame = keyframe_points[i].co[0]

                # if keyframe_points[i].co[0] < keyframe_points[i-1].co[0]:
                #     print('Bad! unsorted !')

                # if val in fcu_orig_data:
                #     i += 1
                #     continue

                val_prev = keyframe_points[i - 1].co[1]
                val_next = keyframe_points[i + 1].co[1]
                
                # 新增判断，线性模式下特别处理
                frame_prev = keyframe_points[i - 1].co[0]
                frame_next = keyframe_points[i + 1].co[0]

                interp = (frame - frame_prev) / (frame_next - frame_prev)
                val_interp = (val_next - val_prev) * interp

                is_linear = keyframe_points[i].interpolation == 'LINEAR' and keyframe_points[i + 1].interpolation == 'LINEAR'

                if abs(val - val_prev) + abs(val - val_next) < eps or\
                    (is_linear and abs(val - val_interp) < eps):
                    need_next_clean_cycle = True
                    keyframe_points.remove(keyframe_points[i])
                    del_count += 1

                else:
                    i += 1
    
    print(f'Cleaning bone curves finish. Del {del_count} Frame.')


def fast_bake_action(
    action_name='', frame_start=1, frame_end=250, frame_step=1,
    use_no_scale=False, use_exist=False, use_disable_constraints=False,
    clean_eps=1e-4, max_clean_cycle=0, use_clean=True,
    use_active=True):
    '''
    快速烘焙
    原理，在action轨道中插入关键帧时，已有的关键帧越多，插入就会变得越来越慢
    我在这里新建了一条NLA轨道，并直接新建足够多的空关键帧，新建完了再直接设置关键帧
    这可以规避因为关键帧越来越多，导致插入越来越慢的问题

    :param action_name                  目标动作名称，如果为空并且 use_exist 为真，则覆盖到活动动作
    :param frame_start                  开始帧位置
    :param frame_start                  结束帧位置
    :param frame_step                   帧步长
    :param use_no_scale                 不使用缩放帧
    :param use_exist                    是否使用已有的action
    :param use_disable_constraints      烘焙完成后是否把约束都禁用掉
    :param use_active                   是否激活新序列
    '''
    if bpy.context.mode not in ['POSE']:
        alert_msg('Error', 'This function can only be used in Pose Mode.')
        return

    # frame_end 也需要包括进来
    frame_end += 1

    scene = bpy.context.scene

    arm_obj = bpy.context.active_object
    if arm_obj is None or arm_obj.type != 'ARMATURE':
        alert_msg('Error', 'The actived object should be a valid armature object.')
        return

    print('Start fast baking.')
    start_time = time.time()

    pose_bones = bpy.context.selected_pose_bones
    bone_names = [b.name for b in pose_bones]

    # 旋转只支持四元数，必须先将骨骼的旋转模式转换为四元数
    for b in pose_bones:
        b.rotation_mode = 'QUATERNION'

    # 骨骼的关键帧
    bone_kps = {}

    for frame_cur in range(frame_start, frame_end, frame_step):
        update_progress(f'Generating visual transform. {frame_cur-frame_start+1}/{frame_end-frame_start}', (frame_cur-frame_start+1) / (frame_end-frame_start))

        # 设定场景帧时，绝对不能使用 scene.frame_cur = xxx
        # 因为它在script代码里面时，不会刷新场景的对象的状态，导致全部对象的姿态全都是错误的（过时的）！
        scene.frame_set(frame_cur)

        # 必须要逐个骨骼进行，不能一下子关掉全部约束！
        for b in pose_bones:
            # 清除约束时保持变换的代码参照官方插件 blender安装目录\3.2\scripts\startup\bl_operators\constraint.py
            
            ori_pose_matrix = b.matrix
            # 使用 convert_space 可以节省很多头发
            world_mat = arm_obj.convert_space(pose_bone=b,  matrix=b.matrix, from_space='POSE', to_space='WORLD')
            # 保存约束状态后，关闭约束
            ctr_state = disable_constraints(b)

            pose_mat = arm_obj.convert_space(pose_bone=b,  matrix=world_mat, from_space='WORLD', to_space='POSE')
            # 直接设定原来的 matrix 就行，location, rotation, scale 会自动计算出来
            b.matrix = pose_mat
            # 一定要使用 copy ，因为这些向量是就地更改的！
            t = b.location.copy()
            r = b.rotation_quaternion.copy()
            s = b.scale.copy()

            # 恢复约束状态
            recover_constraints(b, ctr_state)

            b.matrix = ori_pose_matrix

            bone_kps.setdefault(b.name, [])
            bone_kps[b.name].append([frame_cur, t, r, s])
    finish_progress()

    # 动作名检查
    if action_name == '':
        if use_exist and arm_obj.animation_data.action is not None:
            action_name = arm_obj.animation_data.action.name
        else:
            action_name = 'Action'

    # 使用现有的动作还是新建一个动作
    if use_exist and action_name in bpy.data.actions:
        action = bpy.data.actions[action_name]
    else:
        action = bpy.data.actions.new(name=action_name)
        # 必须要手动设定 name，因为在 new 时，如果名字已存在，会因为自动规避而把自身改名为后缀为 .xxx 的动作，导致名字与需要的不一样
        # 当主动设置name时，则会反过来自动把已存在名字的动作那个进行规避改名，从而保证当前新建的动作名字一定是指定的名字
        action.name = action_name

    all_bone_fcurves = []
    for bone_i, n in enumerate(bone_names):
        update_progress(f'Generating bone curves. {n}', (bone_i+1)/len(bone_names))
        
        if use_no_scale:
            fcurves = [None] * 7    # tx, ty, tz, qw, qx, qy, qz
        else:
            fcurves = [None] * 10   # tx, ty, tz, qw, qx, qy, qz, sx, sy, sz

        # 新建曲线对象
        data_path = f'pose.bones["{n}"].location'
        for axis_i in range(3):
            channel_i = axis_i
            # fcurves[axis_i] = action.fcurves.new(data_path=data_path, index=axis_i, action_group=n)
            fcurves[channel_i] = get_or_create_fcurve(action, n, channel_i, axis_i, data_path=data_path)
            

        data_path = f'pose.bones["{n}"].rotation_quaternion'
        for axis_i in range(4):
            channel_i = 3+axis_i
            # fcurves[3+axis_i] = action.fcurves.new(data_path=data_path, index=axis_i, action_group=n)
            fcurves[channel_i] = get_or_create_fcurve(action, n, channel_i, axis_i, data_path=data_path)
        
        # 如果不要缩放变换
        if not use_no_scale:
            data_path = f'pose.bones["{n}"].scale'
            for axis_i in range(3):
                channel_i = 3+4+axis_i
                # fcurves[3+4+axis_i] = action.fcurves.new(data_path=data_path, index=axis_i, action_group=n)
                fcurves[channel_i] = get_or_create_fcurve(action, n, channel_i, axis_i, data_path=data_path)
        
        cur_bone_kps = bone_kps[n]

        for fc_i, fc in enumerate(fcurves):
            # 支持就地插入
            start_kps = len(fc.keyframe_points)
            fc.keyframe_points.add(len(cur_bone_kps))
            for kp1, kp2 in zip(cur_bone_kps, fc.keyframe_points[start_kps:]):
                frame_id, t, r, s = kp1
                kp1 = [t[0], t[1], t[2], r[0], r[1], r[2], r[3], s[0], s[1], s[2]]

                # 第一个值是帧号，第二个是值
                kp2.co = (frame_id, kp1[fc_i])
                # 默认插值使用线性。
                kp2.interpolation = 'LINEAR'
            # 自动排序关键帧，确保关键帧按时间顺序排列，这在clean时非常重要
            fc.update()
        
        all_bone_fcurves.extend(fcurves)

    finish_progress()
    
    if use_disable_constraints:
        disable_all_constraints(pose_bones)

    if use_active:
        arm_obj.animation_data.action = action
    
    if use_clean:
        clean_fcurve(all_bone_fcurves, clean_eps, max_clean_cycle)
    
    end_time = time.time()
    print(f'Cost time {end_time-start_time:.3f}')

    alert_msg('Info', 'Success.')


def clean_action(clean_eps=1e-4, max_clean_cycle=0):

    if bpy.context.mode not in ['POSE']:
        alert_msg('Error', 'This function can only be used in Pose Mode.')
        return

    arm_obj = bpy.context.active_object
    if arm_obj.type != 'ARMATURE':
        alert_msg('Error', 'The actived object should be a valid armature object.')
        return

    pose_bones = bpy.context.selected_pose_bones
    bone_names = [b.name for b in pose_bones]

    if len(bone_names) == 0:
        alert_msg('Error', 'Please select at least one bone.')
        return

    action = arm_obj.animation_data.action
    if action is None:
        alert_msg('Error', 'No found any active action on actived armature.')
        return

    channels = []
    for group in action.groups:
        if group.name in bone_names:
            for channel in group.channels:
                channels.append(channel)
    
    clean_fcurve(channels, clean_eps, max_clean_cycle)
    alert_msg('Info', 'Success.')
