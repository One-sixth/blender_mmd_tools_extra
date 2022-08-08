import bpy
from bpy.types import Operator
from bpy.props import BoolProperty

from . import rigidbody_func
from .misc import alert_msg, _add_cls_ref


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Rigidbody_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_idname = 'MTE_PT_Rigidbody_Panel'
    # 菜单名字
    bl_label = 'Rigidbody Panel'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator(OT_SelectAllNonBoneRefRigidbody.bl_idname)
        layout.operator(OT_AutoRenameSelectedRigidbody.bl_idname)
        layout.operator(OT_SelectJointBySelectedRigidbody.bl_idname)
        layout.operator(OT_SelectBoneBySelectedRigidbody.bl_idname)


@_add_cls
class OT_SelectAllNonBoneRefRigidbody(Operator):
    bl_idname = 'mte.select_all_non_bone_ref_rigidbody'
    bl_label = 'Select all non bone ref rigid'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        rigidbody_func.select_all_non_bone_ref_rigidbody()
        return {'FINISHED'}


@_add_cls
class OT_AutoRenameSelectedRigidbody(Operator):
    bl_idname = 'mte.auto_rename_selected_rigidbody'
    bl_label = 'Auto rename selected rigidbody'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        rigidbody_func.auto_rename_selected_rigidbody()
        return {'FINISHED'}


@_add_cls
class OT_SelectJointBySelectedRigidbody(Operator):
    bl_idname = 'mte.select_joint_by_selected_rigidbody'
    bl_label = 'Select joint by selected rigidbody'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        rigidbody_func.select_joint_by_selected_rigidbody()
        return {'FINISHED'}


@_add_cls
class OT_SelectBoneBySelectedRigidbody(Operator):
    bl_idname = 'mte.select_bone_by_selected_rigidbody'
    bl_label = 'Select bone by selected rigidbody'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        rigidbody_func.select_bone_by_selected_rigidbody()
        return {'FINISHED'}


# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
