import bpy
from bpy.types import Scene, Operator, PropertyGroup
from bpy.props import BoolProperty, StringProperty, PointerProperty

from . import morph_func
from .misc import alert_msg, _add_cls_ref


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Morph_Prop(PropertyGroup):

    old_related_mesh_patten:                StringProperty(default='*', description='')
    new_related_mesh:                       StringProperty(default='', description='')
    # -------------------------------------------------------------------------------------


@_add_cls
class MTE_Morph_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_idname = 'MTE_PT_Morph_Panel'
    # 菜单名字
    bl_label = 'Morph Tool'

    def draw(self, context):
        scene = context.scene
        prop = scene.mte_morph_prop

        layout = self.layout
        grid = layout.column(align=True)
        grid.prop(prop, 'old_related_mesh_patten', text='old_patten')
        grid.prop_search(prop, 'new_related_mesh', bpy.data, 'meshes', text='new_mesh')
        layout.operator(OT_ReplaceMaterialMorphRelatedMesh.bl_idname)


@_add_cls
class OT_ReplaceMaterialMorphRelatedMesh(Operator):
    bl_idname = 'mte.replace_material_morph_related_mesh'
    bl_label = 'Replace Material Morph Related Mesh'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        prop = scene.mte_morph_prop

        morph_func.replace_material_morph_related_mesh(
            prop.old_related_mesh_patten,
            prop.new_related_mesh,
        )
        return {'FINISHED'}


# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)
    Scene.mte_morph_prop = PointerProperty(type=MTE_Morph_Prop)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
