import bpy
from .misc import alert_msg, filter_mmd_rigidbody
from mmd_tools.core.model import FnModel


def clear_selected_bone_roll():
    if bpy.context.mode != 'EDIT_ARMATURE':
        alert_msg('错误', '只能在骨架编辑模式使用本功能。')
        return

    bone_count = 0

    for b in bpy.context.selected_editable_bones:
        b.roll = 0
        print(f'{b.name}')
        bone_count += 1

    alert_msg('信息', f'成功清除{bone_count}个骨骼翻转角度。')


def symmetric_selected_bones_x():
    if bpy.context.mode != 'EDIT_ARMATURE':
        alert_msg('错误', '只能在骨架编辑模式使用本功能。')
        return
    
    if bpy.context.active_object is None or bpy.context.active_object.type != 'ARMATURE':
        alert_msg('错误', '需要令骨架对象为激活对象。')
        return
    
    arm_obj = bpy.context.active_object
    arm = arm_obj.data

    if bpy.context.selected_editable_bones:
        alert_msg('错误', '需要令骨架对象为激活对象。')
    
    # 对齐时，需要关闭镜像功能
    last_use_mirror_x = arm.use_mirror_x
    arm.use_mirror_x = False

    selected_bone_names = [b.name for b in bpy.context.selected_editable_bones]

    edit_bones = arm.edit_bones

    warning_found_target_bone_in_selected_bone = False

    for n in selected_bone_names:
        tn = None
        if n.endswith('.L'):
            tn = n[:-2] + '.R'
        elif n.endswith('.R'):
            tn = n[:-2] + '.L'
        
        # 检查目标骨骼是否在选中的骨骼中
        if tn in selected_bone_names:
            warning_found_target_bone_in_selected_bone = True
        
        if tn is not None and tn in edit_bones:
            edit_bones[tn].head.x = -edit_bones[n].head.x
            edit_bones[tn].head.yz = edit_bones[n].head.yz
            
            edit_bones[tn].tail.x = -edit_bones[n].tail.x
            edit_bones[tn].tail.yz = edit_bones[n].tail.yz
            
            edit_bones[tn].roll = -edit_bones[n].roll
            
            edit_bones[tn].tail_radius = edit_bones[n].tail_radius
            edit_bones[tn].envelope_distance = edit_bones[n].envelope_distance
            
            # print(f'{n} -> {tn}')

    # 恢复原先的镜像设置
    arm.use_mirror_x = last_use_mirror_x

    if warning_found_target_bone_in_selected_bone:
        alert_msg('警告', '操作完成。但发现目标骨骼在选中的骨骼中，这可能产生意外的结果。')
    else:
        alert_msg('信息', '操作完成。')


def auto_setting_and_hide_tip_bone():
    if bpy.context.mode != 'POSE':
        alert_msg('错误', '只能在姿态模式使用本功能。')
        return
    
    if bpy.context.active_object is None or bpy.context.active_object.type != 'ARMATURE':
        alert_msg('错误', '需要令骨架对象为激活对象。')
        return

    bones = bpy.context.selected_pose_bones

    if len(bones) == 0:
        alert_msg('错误', '请至少选中一个骨骼。')
        return

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
    
    alert_msg('信息', '操作完成')


def select_rigidbody_by_selected_bone():
    if bpy.context.mode not in ['EDIT_ARMATURE', 'POSE']:
        alert_msg('错误', '只能在姿态模式或骨架编辑模式使用本功能。')
        return
    
    arm_obj = bpy.context.active_object
    if arm_obj.type != 'ARMATURE':
        alert_msg('错误', '没有找到激活的骨架对象。')
        return

    bone_names = []
    if bpy.context.selected_editable_bones is not None:
        bone_names += [b.name for b in bpy.context.selected_editable_bones]
    if bpy.context.selected_pose_bones_from_active_object is not None:
        bone_names += [b.name for b in bpy.context.selected_pose_bones_from_active_object]

    mmd_root_obj = FnModel.find_root(arm_obj)
    if mmd_root_obj is None:
        alert_msg('错误', '只能用于MMD模型的骨架')
        return
    
    # 否决的代码
    # rigidbody_group = FnModel.find_rigid_group(mmd_root_obj)
    # if rigidbody_group is None:
    #     alert_msg('错误', '没有找到刚体组')
    #     return
    # rigidbodies = filter_mmd_rigidbody(rigidbody_group.children_recursive)
    
    # 因为找到的刚体数量不完整，所以直接从root_obj开始检索
    rigidbodies = filter_mmd_rigidbody(mmd_root_obj.children_recursive)
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    for rb in rigidbodies:
        if rb.mmd_rigid.bone in bone_names:
            rb.hide_set(False)
            rb.select_set(True)
    
    alert_msg('信息', '操作完成')
