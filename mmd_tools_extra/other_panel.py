import bpy
from bpy.types import Operator
from bpy.props import BoolProperty

from . import other_func
from .misc import alert_msg, _add_cls_ref


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Other_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_idname = 'MTE_PT_Other_Panel'
    # 菜单名字
    bl_label = 'Other Panel'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator(OT_DeleteAllVrmObj.bl_idname)
        layout.operator(OT_DeleteAllInvalidDriver.bl_idname)
        layout.operator(OT_DeleteAllGhostObject.bl_idname)


@_add_cls
class OT_DeleteAllVrmObj(Operator):
    bl_idname = 'mte.delete_all_vrm_obj'
    bl_label = 'Delete all vrm obj'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        other_func.delete_all_vrm_obj()
        return {'FINISHED'}

@_add_cls
class OT_DeleteAllInvalidDriver(Operator):
    bl_idname = 'mte.delete_all_invalid_driver'
    bl_label = 'Delete all invalid driver'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        other_func.delete_all_invalid_driver()
        return {'FINISHED'}

@_add_cls
class OT_DeleteAllGhostObject(Operator):
    bl_idname = 'mte.delete_all_ghost_object'
    bl_label = 'Delete all ghost object'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        other_func.delete_all_ghost_object()
        return {'FINISHED'}

# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
