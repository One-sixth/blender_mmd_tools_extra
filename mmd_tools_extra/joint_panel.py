import bpy
from bpy.types import Operator
from bpy.props import BoolProperty

from . import joint_func
from .misc import alert_msg, _add_cls_ref


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Joint_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_options = {'DEFAULT_CLOSED'}
    bl_idname = 'MTE_PT_Joint_Panel'
    # 菜单名字
    bl_label = 'Joint Panel'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator(OT_SelectAllInvalidJoint.bl_idname)
        layout.operator(OT_AutoRenameSelectedJoint.bl_idname)
        layout.operator(OT_SelectRigidbodyBySelectedJoint.bl_idname)


@_add_cls
class OT_SelectAllInvalidJoint(Operator):
    bl_idname = 'mte.select_all_invalid_joint'
    bl_label = 'Select all invalid joint'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        joint_func.select_all_invalid_joint()
        return {'FINISHED'}


@_add_cls
class OT_AutoRenameSelectedJoint(Operator):
    bl_idname = 'mte.auto_rename_selected_joint'
    bl_label = 'Auto Rename selected joint'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        joint_func.auto_rename_selected_joint()
        return {'FINISHED'}


@_add_cls
class OT_SelectRigidbodyBySelectedJoint(Operator):
    bl_idname = 'mte.select_rigidbody_by_selected_joint'
    bl_label = 'Select rigidbody by selected joint'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        joint_func.select_rigidbody_by_selected_joint()
        return {'FINISHED'}


# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
