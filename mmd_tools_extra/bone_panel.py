import bpy
from bpy.types import Operator
from bpy.props import BoolProperty

from . import bone_func
from .misc import alert_msg, _add_cls_ref


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Bone_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_idname = 'MTE_PT_Bone_Panel'
    # 菜单名字
    bl_label = 'Bone Panel'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator(OT_ClearSelectedBoneRoll.bl_idname)
        layout.operator(OT_SymmetricSelectedBonesX.bl_idname)
        layout.operator(OT_AutoSettingAndHideTipBone.bl_idname)
        layout.operator(OT_SelectRigidbodyBySelectedBone.bl_idname)
        layout.operator(OT_DisconnectAllPhysicalBone.bl_idname)
        layout.operator(OT_CancelDisconnectAllPhysicalBone.bl_idname)


@_add_cls
class OT_ClearSelectedBoneRoll(Operator):
    bl_idname = 'mte.clear_selected_bone_roll'
    bl_label = 'Clear selected bone roll'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bone_func.clear_selected_bone_roll()
        return {'FINISHED'}


@_add_cls
class OT_SymmetricSelectedBonesX(Operator):
    bl_idname = 'mte.symmetric_selected_bones_x'
    bl_label = 'Symmetric selected bones X'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bone_func.symmetric_selected_bones_x()
        return {'FINISHED'}


@_add_cls
class OT_AutoSettingAndHideTipBone(Operator):
    bl_idname = 'mte.auto_setting_and_hide_tip_bone'
    bl_label = 'Auto setting and hide tip bone'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bone_func.auto_setting_and_hide_tip_bone()
        return {'FINISHED'}


@_add_cls
class OT_SelectRigidbodyBySelectedBone(Operator):
    bl_idname = 'mte.select_rigidbody_by_selected_bone'
    bl_label = 'Select rigidbody by selected bone'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bone_func.select_rigidbody_by_selected_bone()
        return {'FINISHED'}


@_add_cls
class OT_DisconnectAllPhysicalBone(Operator):
    bl_idname = 'mte.disconnect_all_physical_bone'
    bl_label = 'Disconnect all physical bone'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bone_func.disconnect_all_physical_bone()
        return {'FINISHED'}


@_add_cls
class OT_CancelDisconnectAllPhysicalBone(Operator):
    bl_idname = 'mte.cancel_disconnect_all_physical_bone'
    bl_label = 'Cancel disconnect all physical bone'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bone_func.cancel_disconnect_all_physical_bone()
        return {'FINISHED'}


# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
