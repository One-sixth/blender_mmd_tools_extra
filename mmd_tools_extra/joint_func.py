import bpy
from .misc import alert_msg, filter_mmd_joint, filter_mmd_rigidbody


def select_all_invalid_joint():
    if bpy.context.mode != 'OBJECT':
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return
    
    obj_list = []

    for obj in bpy.data.objects:
        if obj.rigid_body_constraint is not None and\
            (obj.rigid_body_constraint.object1 is None or\
            obj.rigid_body_constraint.object2 is None):
            obj_list.append(obj)

    for obj in obj_list:
        obj.select_set(True)

    alert_msg('Info', 'Success.')


def auto_rename_selected_joint():
    if bpy.context.mode != 'OBJECT':
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return

    # rb1->rb2->joint
    paired_joints = {}

    name_to_rb = {}

    for obj in filter_mmd_joint(bpy.context.selected_objects):
        if obj.rigid_body_constraint.object1 is not None and\
            obj.rigid_body_constraint.object2 is not None:
            rb1_name = obj.rigid_body_constraint.object1.name
            rb2_name = obj.rigid_body_constraint.object2.name
            
            name_to_rb[rb1_name] = obj.rigid_body_constraint.object1
            name_to_rb[rb2_name] = obj.rigid_body_constraint.object2
            
            paired_joints.setdefault(rb1_name, {})
            paired_joints[rb1_name].setdefault(rb2_name, [])
            
            paired_joints[rb1_name][rb2_name].append(obj)

    idx = 0

    for rb1_name in sorted(list(paired_joints.keys())):
        for rb2_name in sorted(list(paired_joints[rb1_name].keys())):
            
            is_append_joint_i = len(paired_joints[rb1_name][rb2_name]) > 1
            
            for joint_i, joint in enumerate(paired_joints[rb1_name][rb2_name]):
                old_obj_name = joint.name
                old_joint_name = joint.mmd_joint.name_j
                
                rb1_name_2 = name_to_rb[rb1_name].mmd_rigid.name_j
                rb2_name_2 = name_to_rb[rb2_name].mmd_rigid.name_j
                
                new_obj_name = f'{idx}.joint.{rb1_name_2}->{rb2_name_2}'
                if is_append_joint_i:
                    new_obj_name += f'.{joint_i}'
                joint.name = new_obj_name
                
                new_joint_name = f'{rb1_name_2}->{rb2_name_2}'
                if is_append_joint_i:
                    new_joint_name += f'.{joint_i}'
                joint.mmd_joint.name_j = new_joint_name
                
                print(f'rename {old_obj_name}->{new_obj_name} | {old_joint_name}->{new_joint_name}')
                
                idx += 1

    alert_msg('Info', 'Success.')


def select_rigidbody_by_selected_joint():
    if bpy.context.mode != 'OBJECT':
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return

    joints = filter_mmd_joint(bpy.context.selected_objects)

    if len(joints) == 0:
        alert_msg('Error', 'Please select at least one MMD joint.')
        return

    rigidbodies = []

    for j in joints:
        if j.rigid_body_constraint.object1 is not None:
            rigidbodies.append(j.rigid_body_constraint.object1)
        if j.rigid_body_constraint.object2 is not None:
            rigidbodies.append(j.rigid_body_constraint.object2)
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    for rb in rigidbodies:
        rb.hide_set(False)
        rb.select_set(True)
    
    alert_msg('Info', 'Success.')
