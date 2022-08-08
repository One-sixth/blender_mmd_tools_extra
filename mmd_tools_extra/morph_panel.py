import bpy
from bpy.types import Scene, Operator, PropertyGroup
from bpy.props import BoolProperty, StringProperty, PointerProperty

from . import morph_func
from .misc import alert_msg, _add_cls_ref


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Morph_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_idname = 'MTE_PT_Morph_Panel'
    # 菜单名字
    bl_label = 'Morph Panel'

    def draw(self, context):
        layout = self.layout
        layout.operator(ReplaceMaterialMorphRelatedMeshDialogOperator.bl_idname)


@_add_cls
class ReplaceMaterialMorphRelatedMeshDialogOperator(Operator):
    bl_idname = "object.replace_material_morph_related_mesh_dialog"
    bl_label = "Replace Material Morph Related Mesh Dialog"

    old_related_mesh_patten:                StringProperty(name='old mesh name patten', default='*', description='')
    new_related_mesh:                       StringProperty(name='new mesh name', default='', description='')

    def execute(self, context):
        morph_func.replace_material_morph_related_mesh(
            self.old_related_mesh_patten,
            self.new_related_mesh,
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
