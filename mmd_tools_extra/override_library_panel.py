import bpy
from bpy.types import Operator
from bpy.props import BoolProperty, StringProperty, FloatProperty, IntProperty

from . import override_library_func
from .misc import alert_msg, _add_cls_ref


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_OverrideLibrary_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_options = {'DEFAULT_CLOSED'}
    bl_idname = 'MTE_PT_OverrideLibrary_Panel'
    # 菜单名字
    bl_label = 'OverrideLibrary Panel'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator(BatchCreateOverrideLibraryDialogOperator.bl_idname)
        layout.operator(OT_AllMakeLocal.bl_idname)


@_add_cls
class BatchCreateOverrideLibraryDialogOperator(Operator):
    bl_idname = 'object.batch_create_override_library_dialog'
    bl_label = 'Batch Create OverrideLibrary Dialog'

    '''
    :param make_local
    :param recusive_children
    :param include_mesh
    :param include_mesh_data
    :param include_material
    :param include_armature
    :param include_armature_data
    :param include_empty
    :param include_camera
    :param include_camera_data
    '''

    make_local:                 BoolProperty(name='Make local', default=False)
    recusive_children:          BoolProperty(name='Recusive children', default=True)
    include_mesh:               BoolProperty(name='Mesh', default=True)
    include_mesh_data:          BoolProperty(name='Mesh data', default=True)
    include_material:           BoolProperty(name='Material', default=True)
    include_armature:           BoolProperty(name='Armature', default=True)
    include_armature_data:      BoolProperty(name='Armature data', default=True)
    include_empty:              BoolProperty(name='Empty', default=True)
    include_camera:             BoolProperty(name='Camera', default=True)
    include_camera_data:        BoolProperty(name='Camera data', default=True)

    def execute(self, context):
        override_library_func.batch_create_override_library(
            self.make_local,
            self.recusive_children,
            self.include_mesh, self.include_mesh_data, self.include_material,
            self.include_armature, self.include_armature_data,
            self.include_empty,
            self.include_camera, self.include_camera_data,
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


@_add_cls
class OT_AllMakeLocal(Operator):
    bl_idname = 'mte.all_make_local'
    bl_label = 'All make local'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.make_local(type='ALL')
        return {'FINISHED'}


# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
