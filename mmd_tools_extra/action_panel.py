import bpy
from bpy.types import Operator
from bpy.props import BoolProperty, StringProperty, FloatProperty, IntProperty

from . import action_func
from .misc import alert_msg, _add_cls_ref


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Action_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_idname = 'MTE_PT_Action_Panel'
    # 菜单名字
    bl_label = 'Action Tool'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator(FastBakeActionDialogOperator.bl_idname)


@_add_cls
class FastBakeActionDialogOperator(Operator):
    bl_idname = "object.fast_bake_action_dialog"
    bl_label = "Fast Bake Action Dialog"

    action_name:                StringProperty(name="Action name", default='')
    frame_start:                IntProperty(name="Frame start", default=-1)
    frame_end:                  IntProperty(name="Frame end", default=-2)
    frame_step:                 IntProperty(name="Frame step", default=1)
    use_no_scale:               BoolProperty(name="No scale", default=False)
    use_exist:                  BoolProperty(name="Use exist", default=False)
    use_disable_constraints:    BoolProperty(name="Disable constraints", default=True)
    use_clean:                  BoolProperty(name="Clean", default=True)
    use_active:                 BoolProperty(name="Active", default=True)

    def execute(self, context):
        action_func.fast_bake_action(
            self.action_name, self.frame_start, self.frame_end, self.frame_step,
            self.use_no_scale, self.use_exist, self.use_disable_constraints, self.use_clean, self.use_active)
        return {'FINISHED'}

    def invoke(self, context, event):
        if self.frame_end < self.frame_start and self.frame_start == -1 and self.frame_end == -2:
            self.frame_start = bpy.context.scene.frame_start
            self.frame_end = bpy.context.scene.frame_end

        wm = context.window_manager
        return wm.invoke_props_dialog(self)

# @_add_cls
# class OT_FastBakeAction(Operator):
#     bl_idname = 'mte.seg_bake'
#     bl_label = 'Segment Action'
#     bl_options = {'REGISTER', 'UNDO'}

#     def execute(self, context):
#         action_func.seg_bake()
#         return {'FINISHED'}


# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
