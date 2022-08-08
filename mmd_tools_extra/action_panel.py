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
    bl_label = 'Action Panel'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator(FastBakeActionDialogOperator.bl_idname)
        layout.operator(CleanActionDialogOperator.bl_idname)


@_add_cls
class FastBakeActionDialogOperator(Operator):
    bl_idname = "object.fast_bake_action_dialog"
    bl_label = "Fast Bake Action Dialog"

    action_name:                StringProperty(name="Action name", default='')
    frame_start:                IntProperty(name="Frame start", default=-1)
    frame_end:                  IntProperty(name="Frame end", default=-2)
    frame_step:                 IntProperty(name="Frame step", default=1)
    use_no_scale:               BoolProperty(name="No scale", default=False)
    use_exist:                  BoolProperty(name="Override existing action", default=False)
    use_disable_constraints:    BoolProperty(name="Disable constraints after baking", default=True)
    clean_eps:                  FloatProperty(name="Clean eps", default=1e-4)
    max_clean_cycle:            IntProperty(name="Max clean cycle", default=0)
    use_clean:                  BoolProperty(name="Clean redundant frame", default=True)
    use_active:                 BoolProperty(name="Active action", default=True)

    def execute(self, context):
        action_func.fast_bake_action(
            self.action_name, self.frame_start, self.frame_end, self.frame_step,
            self.use_no_scale, self.use_exist, self.use_disable_constraints,
            self.clean_eps, self.max_clean_cycle, self.use_clean,
            self.use_active)
        return {'FINISHED'}

    def invoke(self, context, event):
        if self.frame_end < self.frame_start and self.frame_start == -1 and self.frame_end == -2:
            self.frame_start = bpy.context.scene.frame_start
            self.frame_end = bpy.context.scene.frame_end

        wm = context.window_manager
        return wm.invoke_props_dialog(self)


@_add_cls
class CleanActionDialogOperator(Operator):
    bl_idname = "object.clean_action_dialog"
    bl_label = "Clean Action Dialog"

    clean_eps:                  FloatProperty(name="Clean eps", default=1e-4)
    max_clean_cycle:            IntProperty(name="Max clean cycle", default=0)

    def execute(self, context):
        action_func.clean_action(self.clean_eps, self.max_clean_cycle)
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
