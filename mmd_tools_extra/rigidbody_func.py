import bpy
from .misc import alert_msg, filter_mmd_rigidbody, filter_mmd_joint
from mmd_tools.core.model import FnModel


def select_all_non_bone_ref_rigidbody(delete=False):
    if bpy.context.mode != 'OBJECT':
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return

    obj_list = []

    for obj in filter_mmd_rigidbody(bpy.context.visible_objects):

        mmd_root_obj = FnModel.find_root(obj)
        if mmd_root_obj is None:
            continue

        arm_obj = FnModel.find_armature(mmd_root_obj)
        if arm_obj is None:
            obj_list.append(obj)
            continue

        arm = arm_obj.data
        bone_names = [b.name for b in arm.bones]
        if obj.mmd_rigid.bone not in bone_names:
            obj_list.append(obj)

    for obj in obj_list:
        print('select', obj.name)
        obj.select_set(True)

    alert_msg('Info', 'Success.')


def auto_rename_selected_rigidbody():
    if bpy.context.mode != 'OBJECT':
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return

    bonename_rigidbodies = {}

    for obj in filter_mmd_rigidbody(bpy.context.selected_objects):
        if obj.mmd_rigid.bone != '':
            bonename = obj.mmd_rigid.bone
        else:
            bonename = obj.mmd_rigid.name_j
        bonename_rigidbodies.setdefault(bonename, [])
        bonename_rigidbodies[bonename].append(obj)

    idx = 0

    sorted_bonenames = sorted(list(bonename_rigidbodies.keys()))

    for bonename in sorted_bonenames:
        is_append_rb_i = len(bonename_rigidbodies[bonename]) > 1
        for rb_i, rb in enumerate(bonename_rigidbodies[bonename]):
            old_obj_name = rb.name
            old_rb_name = rb.mmd_rigid.name_j
            
            new_obj_name = f'{idx}.rigid.{bonename}'
            if is_append_rb_i:
                new_obj_name += f'.{rb_i}'
            rb.name = new_obj_name
            
            new_rb_name = f'{bonename}'
            if is_append_rb_i:
                new_rb_name += f'.{rb_i}'
            rb.mmd_rigid.name_j = new_rb_name
            
            print(f'rename {old_obj_name}->{new_obj_name} | {old_rb_name}->{new_rb_name}')
            
            idx += 1

    alert_msg('Info', 'Success.')


def select_joint_by_selected_rigidbody():
    if bpy.context.mode != 'OBJECT':
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return

    rigidbodies = filter_mmd_rigidbody(bpy.context.selected_objects)
    joints = []

    for j in filter_mmd_joint(bpy.data.objects):
        if j.rigid_body_constraint.object1 in rigidbodies or\
            j.rigid_body_constraint.object2 in rigidbodies:
            joints.append(j)
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    for j in joints:
        j.hide_set(False)
        j.select_set(True)
    
    alert_msg('Info', 'Success.')


def select_bone_by_selected_rigidbody():
    if bpy.context.mode != 'OBJECT':
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return

    rigidbodies = filter_mmd_rigidbody(bpy.context.selected_objects)

    if len(rigidbodies) == 0:
        alert_msg('Error', 'Please select at least one MMD rigidbody.')
        return

    mmd_root_obj = FnModel.find_root(rigidbodies[0])
    if mmd_root_obj is None:
        alert_msg('Error', 'The MMD root object associated with the MMD rigidbody does not exist.')
        return

    arm_obj = FnModel.find_armature(mmd_root_obj)
    if arm_obj is None:
        alert_msg('Error', 'The MMD armature object associated with the MMD rigidbody does not exist.')
        return

    bone_names = []
    for rb in rigidbodies:
        bone_names.append(rb.mmd_rigid.bone)
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    arm_obj.hide_set(False)
    arm_obj.select_set(True)
    bpy.context.view_layer.objects.active = arm_obj
    bpy.ops.object.mode_set(mode='EDIT')

    arm = arm_obj.data

    for bone in arm.edit_bones:
        if bone.name in bone_names:
            bone.hide = False
            bone.select = True
        else:
            bone.select = False
            bone.select_head = False
            bone.select_tail = False
    
    alert_msg('Info', 'Success.')
