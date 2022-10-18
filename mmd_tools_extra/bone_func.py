import bpy
from .misc import alert_msg, filter_mmd_rigidbody, find_mmd_root_obj, symmetric_x_blender_name, symmetric_x_mmd_name_j, symmetric_x_vector
from mmd_tools.core.model import FnModel


def clear_selected_bone_roll():
    if bpy.context.mode != 'EDIT_ARMATURE':
        alert_msg('Error', 'This function can only be used in Armature Edit Mode.')
        return

    bone_count = 0
    for b in bpy.context.selected_editable_bones:
        b.roll = 0
        print(f'{b.name}')
        bone_count += 1

    print(f'Clear {bone_count} bone roll.')
    alert_msg('Info', 'Success.')


def symmetric_selected_bones_x():
    if bpy.context.mode != 'EDIT_ARMATURE':
        alert_msg('Error', 'This function can only be used in Armature Edit Mode.')
        return
    
    if bpy.context.active_object is None or bpy.context.active_object.type != 'ARMATURE':
        alert_msg('Error', 'The actived object should be a valid armature object.')
        return
    
    arm_obj = bpy.context.active_object
    arm = arm_obj.data

    if bpy.context.selected_editable_bones:
        alert_msg('Error', 'Please select at least one bone.')
    
    # 对齐时，需要关闭镜像功能
    last_use_mirror_x = arm.use_mirror_x
    arm.use_mirror_x = False

    selected_bone_names = [b.name for b in bpy.context.selected_editable_bones]

    edit_bones = arm.edit_bones
    pose_bones = arm_obj.pose.bones

    warning_found_target_bone_in_selected_bone = False

    for n in selected_bone_names:
        tn = symmetric_x_blender_name(n)
        
        # 检查目标骨骼是否在选中的骨骼中
        if tn in selected_bone_names:
            warning_found_target_bone_in_selected_bone = True
        
        if tn is not None and tn in edit_bones:
            edit_bones[tn].head = symmetric_x_vector(edit_bones[n].head)
            edit_bones[tn].tail = symmetric_x_vector(edit_bones[n].tail)
            edit_bones[tn].roll = -edit_bones[n].roll
            edit_bones[tn].tail_radius = edit_bones[n].tail_radius
            edit_bones[tn].envelope_distance = edit_bones[n].envelope_distance
            # print(f'{n} -> {tn}')

        # 处理mmd_bone
        pose_bones[tn].mmd_bone.name_j = symmetric_x_mmd_name_j(pose_bones[n].mmd_bone.name_j)
        pose_bones[tn].mmd_bone.transform_order = pose_bones[n].mmd_bone.transform_order
        pose_bones[tn].mmd_bone.is_controllable = pose_bones[n].mmd_bone.is_controllable
        pose_bones[tn].mmd_bone.transform_after_dynamics = pose_bones[n].mmd_bone.transform_after_dynamics
        pose_bones[tn].mmd_bone.is_tip = pose_bones[n].mmd_bone.is_tip

        pose_bones[tn].mmd_bone.enabled_fixed_axis = pose_bones[n].mmd_bone.enabled_fixed_axis
        pose_bones[tn].mmd_bone.fixed_axis = symmetric_x_vector(pose_bones[n].mmd_bone.fixed_axis)

        pose_bones[tn].mmd_bone.enabled_local_axes = pose_bones[n].mmd_bone.enabled_local_axes
        pose_bones[tn].mmd_bone.local_axis_x = symmetric_x_vector(pose_bones[n].mmd_bone.local_axis_x)
        pose_bones[tn].mmd_bone.local_axis_z = symmetric_x_vector(pose_bones[n].mmd_bone.local_axis_z)

        tmp_bone_name = symmetric_x_blender_name(pose_bones[n].mmd_bone.additional_transform_bone)
        if tmp_bone_name in edit_bones:
            pose_bones[tn].mmd_bone.additional_transform_bone = tmp_bone_name
            pose_bones[tn].mmd_bone.has_additional_location = pose_bones[n].mmd_bone.has_additional_location
            pose_bones[tn].mmd_bone.has_additional_rotation = pose_bones[n].mmd_bone.has_additional_rotation
        else:
            pose_bones[tn].mmd_bone.additional_transform_bone = ''
            pose_bones[tn].mmd_bone.has_additional_location = False
            pose_bones[tn].mmd_bone.has_additional_rotation = False
        pose_bones[tn].mmd_bone.additional_transform_influence = pose_bones[n].mmd_bone.additional_transform_influence

    # 更新附加变换设定
    bpy.ops.mmd_tools.apply_additional_transform()

    # 恢复原先的镜像设置
    arm.use_mirror_x = last_use_mirror_x

    if warning_found_target_bone_in_selected_bone:
        alert_msg('Warning', 'Success. But the target bone is found to be among the selected bones, which may have unexpected results.')
    else:
        alert_msg('Info', 'Success.')


def auto_setting_and_hide_tip_bone():
    if bpy.context.mode != 'POSE':
        alert_msg('Error', 'This function can only be used in Pose Mode.')
        return
    
    if bpy.context.active_object is None or bpy.context.active_object.type != 'ARMATURE':
        alert_msg('Error', 'The actived object should be a valid armature object.')
        return

    arm_obj = bpy.context.active_object
    bones = arm_obj.pose.bones

    for bone in bones:
        mbone = bone.mmd_bone
        # print(f'{mbone.name_j}')
        
        # 检查 日文名 后缀是否为 “先”
        if mbone.name_j.endswith('先'):
            if not mbone.is_tip:
                # print(f'setting {mbone.name_j} is_tip to True')
                mbone.is_tip = True
        
        # 检查是否为尖端骨骼
        if mbone.is_tip:
            if mbone.is_controllable:
                # print(f'setting {mbone.name_j} is_controllable to False')
                mbone.is_controllable = False
            
            # 设定骨骼的隐藏属性。姿态模式不可见，编辑模式可见；同时，mmd里面，不可见。
            if not bone.bone.hide:
                # print(f'setting {mbone.name_j} hide to True')
                bone.bone.hide = True
    
    alert_msg('Info', 'Success.')


def hide_all_uncontrollable_bone():
    if bpy.context.mode != 'POSE':
        alert_msg('Error', 'This function can only be used in Pose Mode.')
        return
    
    if bpy.context.active_object is None or bpy.context.active_object.type != 'ARMATURE':
        alert_msg('Error', 'The actived object should be a valid armature object.')
        return

    arm_obj = bpy.context.active_object
    bones = arm_obj.pose.bones

    for bone in bones:
        mbone = bone.mmd_bone
        # print(f'{mbone.name_j}')

        # 检查骨骼是否为不可控制
        if not mbone.is_controllable or bone.is_mmd_shadow_bone:
            # 设定骨骼的隐藏属性。姿态模式不可见，编辑模式可见；同时，mmd里面，不可见。
            if not bone.bone.hide:
                # print(f'setting {mbone.name_j} hide to True')
                bone.bone.hide = True
    
    alert_msg('Info', 'Success.')


def hide_all_physics_bone(use_pose_mode):
    if bpy.context.mode != 'OBJECT':
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return

    from .rigidbody_func import select_rigidbody_by_physics_type, select_bone_by_selected_rigidbody
    select_rigidbody_by_physics_type(False, True, True)
    select_bone_by_selected_rigidbody()

    if use_pose_mode:
        bpy.ops.object.posemode_toggle()
        for bone in bpy.context.selected_pose_bones:
            bone.bone.hide = True
    else:
        # edit mode
        for bone in bpy.context.selected_editable_bones:
            bone.hide = True
    
    root_obj = find_mmd_root_obj(bpy.context.active_object)
    if root_obj is not None and hasattr(root_obj, 'mmd_root'):
        root_obj.mmd_root.show_rigid_bodies = False

    alert_msg('Info', 'Success.')


def select_rigidbody_by_selected_bone():
    if bpy.context.mode not in ['EDIT_ARMATURE', 'POSE']:
        alert_msg('Error', 'This function can only be used in Pose Mode and Armature Edit Mode.')
        return
    
    arm_obj = bpy.context.active_object
    if arm_obj is None or arm_obj.type != 'ARMATURE':
        alert_msg('Error', 'The actived object should be a valid armature object.')
        return

    bone_names = []
    if bpy.context.selected_editable_bones is not None:
        bone_names += [b.name for b in bpy.context.selected_editable_bones]
    if bpy.context.selected_pose_bones_from_active_object is not None:
        bone_names += [b.name for b in bpy.context.selected_pose_bones_from_active_object]

    mmd_root_obj = FnModel.find_root(arm_obj)
    if mmd_root_obj is None:
        alert_msg('Error', 'This function can only be used for armature of MMD model.')
        return

    # 因为找到的刚体数量不完整，所以直接从root_obj开始检索
    rigidbodies = filter_mmd_rigidbody(mmd_root_obj.children_recursive)

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    for rb in rigidbodies:
        if rb.mmd_rigid.bone in bone_names:
            rb.hide_set(False)
            rb.select_set(True)
    
    alert_msg('Info', 'Success.')


def disconnect_all_physical_bone():
    # 断离所有物理骨骼，不影响模型导出
    # ref issue https://github.com/UuuNyaa/blender_mmd_tools/issues/50

    if bpy.context.mode not in ['EDIT_ARMATURE']:
        alert_msg('Error', 'This function can only be used in Armature Edit Mode.')
        return
    
    arm_obj = bpy.context.active_object
    if arm_obj is None or arm_obj.type != 'ARMATURE':
        alert_msg('Error', 'The actived object should be a valid armature object.')
        return

    mmd_root_obj = FnModel.find_root(arm_obj)
    if mmd_root_obj is None:
        alert_msg('Error', 'This function can only be used for armature of MMD model.')
        return

    rigidbodies = filter_mmd_rigidbody(mmd_root_obj.children_recursive)
    
    bone_names = []

    for rb in rigidbodies:
        if rb.mmd_rigid.type == '1':
            if rb.mmd_rigid.bone != '':
                bone_names.append(rb.mmd_rigid.bone)

    for bone in arm_obj.data.edit_bones:
        if bone.name in bone_names:
            bone['mmd_bone_use_connect'] = 1
            bone.use_connect = False

    alert_msg('Info', 'Success.')


def cancel_disconnect_all_physical_bone():
    # 取消断离所有物理骨骼
    # ref issue https://github.com/UuuNyaa/blender_mmd_tools/issues/50

    if bpy.context.mode not in ['EDIT_ARMATURE']:
        alert_msg('Error', 'This function can only be used in Armature Edit Mode.')
        return
    
    arm_obj = bpy.context.active_object
    if arm_obj is None or arm_obj.type != 'ARMATURE':
        alert_msg('Error', 'The actived object should be a valid armature object.')
        return

    for bone in arm_obj.data.edit_bones:
        if 'mmd_bone_use_connect' in bone.keys():
            bone.use_connect = bool(bone['mmd_bone_use_connect'])
            del bone['mmd_bone_use_connect']

    alert_msg('Info', 'Success.')
