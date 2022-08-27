import bpy
from bpy.types import PropertyGroup, Panel, Operator, Scene
from bpy.props import BoolProperty, IntProperty, FloatProperty, EnumProperty, FloatVectorProperty, StringProperty, PointerProperty

from fnmatch import fnmatch
from . import material_func
from .misc import alert_msg, _add_cls_ref, get_hide_icon
from mmd_tools.core import material as mmd_tool_material


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Material_Prop(PropertyGroup):

    match_material_name:        StringProperty(default='*', description='')
    match_name_j:               BoolProperty(default=False, description='')
    # -------------------------------------------------------------------------------------

    use_diffuse_color:          BoolProperty(default=False, description='')
    use_specular_color:         BoolProperty(default=False, description='')
    use_ambient_color:          BoolProperty(default=False, description='')
    use_alpha:                  BoolProperty(default=False, description='')
    use_shininess:              BoolProperty(default=False, description='')
    use_double_side:            BoolProperty(default=False, description='')
    use_ground_shadow:          BoolProperty(default=False, description='')
    use_self_shadow_map:        BoolProperty(default=False, description='')
    use_self_shadow:            BoolProperty(default=False, description='')
    use_outline:                BoolProperty(default=False, description='')
    use_outline_color:          BoolProperty(default=False, description='')
    use_outline_weight:         BoolProperty(default=False, description='')
    use_base_tex:               BoolProperty(default=False, description='')
    use_sphere_tex:             BoolProperty(default=False, description='')
    use_sphere_tex_type:        BoolProperty(default=False, description='')
    use_is_shared_toon_tex:     BoolProperty(default=False, description='')
    use_shared_toon_tex_id:     BoolProperty(default=False, description='')
    use_toon_tex:               BoolProperty(default=False, description='')

    new_diffuse_color:          FloatVectorProperty(default=(1., 1., 1.), subtype='COLOR', min=0, max=1, description='')
    new_specular_color:         FloatVectorProperty(default=(0., 0., 0.), subtype='COLOR', min=0, max=1, description='')
    new_ambient_color:          FloatVectorProperty(default=(0.5, 0.5, 0.5), subtype='COLOR', min=0, max=1, description='')
    new_alpha:                  FloatProperty(default=1., min=0, max=1, description='')
    new_shininess:              FloatProperty(default=5., min=0, soft_max=512, description='')
    new_double_side:            BoolProperty(default=False, description='')
    new_ground_shadow:          BoolProperty(default=True, description='')
    new_self_shadow_map:        BoolProperty(default=True, description='')
    new_self_shadow:            BoolProperty(default=True, description='')
    new_outline:                BoolProperty(default=True, description='')
    new_outline_color:          FloatVectorProperty(default=(0., 0., 0., 1.), subtype='COLOR', size=4, min=0, max=1, description='')
    new_outline_weight:         FloatProperty(default=1., min=0, soft_max=1, description='')
    new_base_tex:               StringProperty(default='', subtype='FILE_PATH', description='')
    new_sphere_tex:             StringProperty(default='', subtype='FILE_PATH', description='')
    new_sphere_tex_type:        EnumProperty(default=str(mmd_tool_material.SPHERE_MODE_OFF), description='Choose sphere texture blend type',
                                    items=[
                                        (str(mmd_tool_material.SPHERE_MODE_OFF),    'Off',        '', 1),
                                        (str(mmd_tool_material.SPHERE_MODE_MULT),   'Multiply',   '', 2),
                                        (str(mmd_tool_material.SPHERE_MODE_ADD),    'Add',        '', 3),
                                        (str(mmd_tool_material.SPHERE_MODE_SUBTEX), 'SubTexture', '', 4),
                                    ]
                                )
    new_is_shared_toon_tex:     BoolProperty(default=True, description='')
    new_shared_toon_tex_id:     IntProperty(default=0, min=0, max=9, description='Shared toon texture id (toon01.bmp ~ toon10.bmp)')
    new_toon_tex:               StringProperty(default='', subtype='FILE_PATH', description='')
    # -------------------------------------------------------------------------------------

    delimiter_str:              StringProperty(default='.', description='')
    use_alert_name_j:           BoolProperty(default=False, description='')
    # -------------------------------------------------------------------------------------

    use_del_prefix:             BoolProperty(default=False, description='')
    use_del_suffix:             BoolProperty(default=False, description='')
    # -------------------------------------------------------------------------------------

    use_add_prefix:             BoolProperty(default=False, description='')
    use_add_suffix:             BoolProperty(default=False, description='')

    new_add_prefix:             StringProperty(default='', description='')
    new_add_suffix:             StringProperty(default='', description='')
    # -------------------------------------------------------------------------------------

    use_replace_str:            BoolProperty(default=False, description='')
    old_replace_str:            StringProperty(default='', description='')
    new_replace_str:            StringProperty(default='', description='')
    # -------------------------------------------------------------------------------------

    use_backface_culling:       BoolProperty(default=False, description='')
    new_backface_culling:       BoolProperty(default=False, description='')

    use_blend_method:           BoolProperty(default=False, description='')
    new_blend_method:           EnumProperty(default='HASHED', description='Blend Method',
                                    items=[('OPAQUE', 'OPAQUE', ''), ('CLIP', 'CLIP', ''), ('HASHED', 'HASHED', ''), ('BLEND', 'BLEND', '')]
                                )
    
    use_shadow_method:          BoolProperty(default=False, description='')
    new_shadow_method:          EnumProperty(default='NONE', description='Shadow Method',
                                    items=[('NONE', 'NONE', ''), ('OPAQUE', 'OPAQUE', ''), ('CLIP', 'CLIP', ''), ('HASHED', 'HASHED', '')]
                                )
    
    use_alpha_threshold:        BoolProperty(default=False, description='')
    new_alpha_threshold:        FloatProperty(default=0.5, min=0, max=1, description='')

    use_screen_refraction:      BoolProperty(default=False, description='')
    new_screen_refraction:      BoolProperty(default=True, description='')

    use_refraction_depth:       BoolProperty(default=False, description='')
    new_refraction_depth:       FloatProperty(default=0, min=0, soft_max=100, description='')

    use_sss_translucency:       BoolProperty(default=False, description='')
    new_sss_translucency:       BoolProperty(default=True, description='')

    use_pass_index:             BoolProperty(default=False, description='')
    new_pass_index:             IntProperty(default=0, min=0, soft_max=16, max=32767, description='')
    # -------------------------------------------------------------------------------------


@_add_cls
class MTE_Material_Panel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_idname = 'MTE_PT_Material_Panel'
    # 菜单名字
    bl_label = 'Material Panel'

    def draw(self, context):
        scene = context.scene
        prop = scene.mte_material_prop

        layout = self.layout
        # -----------------------------------------------------------------------------------------
        layout.label(text='Batch alter material props.')
        grid = layout.column(align=True)

        row = grid.row(align=False)
        row.prop(prop, 'match_material_name', text='patten')
        row.prop(prop, 'match_name_j', text='jp_name')

        grid.separator()
        # -----------------------------------------------------------------------------------------

        row = grid.row(align=True)
        row.prop(prop, 'use_diffuse_color', text='', icon=get_hide_icon(prop.use_diffuse_color))
        row.prop(prop, 'new_diffuse_color', text='diffuse')

        row = grid.row(align=True)
        row.prop(prop, 'use_specular_color', text='', icon=get_hide_icon(prop.use_specular_color))
        row.prop(prop, 'new_specular_color', text='specular')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_ambient_color', text='', icon=get_hide_icon(prop.use_ambient_color))
        row.prop(prop, 'new_ambient_color', text='ambient')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_alpha', text='', icon=get_hide_icon(prop.use_alpha))
        row.prop(prop, 'new_alpha', text='alpha')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_shininess', text='', icon=get_hide_icon(prop.use_shininess))
        row.prop(prop, 'new_shininess', text='shininess')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_double_side', text='', icon=get_hide_icon(prop.use_double_side))
        row.prop(prop, 'new_double_side', text='double side')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_ground_shadow', text='', icon=get_hide_icon(prop.use_ground_shadow))
        row.prop(prop, 'new_ground_shadow', text='ground shadow')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_self_shadow_map', text='', icon=get_hide_icon(prop.use_self_shadow_map))
        row.prop(prop, 'new_self_shadow_map', text='self shadow map')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_self_shadow', text='', icon=get_hide_icon(prop.use_self_shadow))
        row.prop(prop, 'new_self_shadow', text='self shadow')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_outline', text='', icon=get_hide_icon(prop.use_outline))
        row.prop(prop, 'new_outline', text='outline')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_outline_color', text='', icon=get_hide_icon(prop.use_outline_color))
        row.prop(prop, 'new_outline_color', text='outline color')
        
        row = grid.row(align=True)
        row.prop(prop, 'use_outline_weight', text='', icon=get_hide_icon(prop.use_outline_weight))
        row.prop(prop, 'new_outline_weight', text='outline weight', slider=True)
        
        # -----------------------------------------------------------------------------------------
        row = grid.row(align=True)
        row.prop(prop, 'use_base_tex', text='', icon=get_hide_icon(prop.use_base_tex))
        row.prop(prop, 'new_base_tex', text='base tex')

        row = grid.row(align=True)
        row.prop(prop, 'use_sphere_tex', text='', icon=get_hide_icon(prop.use_sphere_tex))
        row.prop(prop, 'new_sphere_tex', text='sphere tex')

        row = grid.row(align=True)
        row.prop(prop, 'use_sphere_tex_type', text='', icon=get_hide_icon(prop.use_sphere_tex_type))
        row.label(text='sphere tex type')
        row.prop(prop, 'new_sphere_tex_type', text='sphere tex type', expand=True)

        row = grid.row(align=True)
        row.prop(prop, 'use_is_shared_toon_tex', text='', icon=get_hide_icon(prop.use_is_shared_toon_tex))
        row.prop(prop, 'new_is_shared_toon_tex', text='is shared toon tex')

        row = grid.row(align=True)
        row.prop(prop, 'use_shared_toon_tex_id', text='', icon=get_hide_icon(prop.use_shared_toon_tex_id))
        row.prop(prop, 'new_shared_toon_tex_id', text='shared toon tex id')

        row = grid.row(align=True)
        row.prop(prop, 'use_toon_tex', text='', icon=get_hide_icon(prop.use_toon_tex))
        row.prop(prop, 'new_toon_tex', text='toon tex')

        # -----------------------------------------------------------------------------------------
        grid.separator()

        row = grid.row(align=True)
        row.prop(prop, 'delimiter_str', text='delimiter str')
        row = grid.row(align=True)
        row.prop(prop, 'use_alert_name_j', text='alert_name_j', icon=get_hide_icon(prop.use_alert_name_j))

        row = grid.row(align=True)
        row.prop(prop, 'use_del_prefix', text='del prefix', icon=get_hide_icon(prop.use_del_prefix))
        row.prop(prop, 'use_del_suffix', text='del suffix', icon=get_hide_icon(prop.use_del_suffix))

        # -----------------------------------------------------------------------------------------
        grid.separator()

        row = grid.row(align=True)
        row.prop(prop, 'use_add_prefix', text='', icon=get_hide_icon(prop.use_add_prefix))
        row.prop(prop, 'new_add_prefix', text='new prefix')

        row = grid.row(align=True)
        row.prop(prop, 'use_add_suffix', text='', icon=get_hide_icon(prop.use_add_suffix))
        row.prop(prop, 'new_add_suffix', text='new suffix')

        # -----------------------------------------------------------------------------------------
        grid.separator()

        grid.label(text='replace str')
        row = grid.row(align=True)
        row.prop(prop, 'use_replace_str', text='', icon=get_hide_icon(prop.use_replace_str))
        row.prop(prop, 'old_replace_str', text='old str')
        row.prop(prop, 'new_replace_str', text='new str')

        # -----------------------------------------------------------------------------------------
        grid.separator()

        row = grid.row(align=True)
        row.prop(prop, 'use_backface_culling', text='', icon=get_hide_icon(prop.use_backface_culling))
        row.prop(prop, 'new_backface_culling', text='backface culling')

        row = grid.row(align=True)
        row.prop(prop, 'use_blend_method', text='', icon=get_hide_icon(prop.use_blend_method))
        row.label(text='blend method')
        row.prop(prop, 'new_blend_method', text='blend method', expand=True)

        row = grid.row(align=True)
        row.prop(prop, 'use_shadow_method', text='', icon=get_hide_icon(prop.use_shadow_method))
        row.label(text='shadow method')
        row.prop(prop, 'new_shadow_method', text='shadow method', expand=True)
        
        row = grid.row(align=True)
        row.prop(prop, 'use_alpha_threshold', text='', icon=get_hide_icon(prop.use_alpha_threshold))
        row.prop(prop, 'new_alpha_threshold', text='alpha threshold', slider=True)
        
        row = grid.row(align=True)
        row.prop(prop, 'use_screen_refraction', text='', icon=get_hide_icon(prop.use_screen_refraction))
        row.prop(prop, 'new_screen_refraction', text='screen refraction')

        row = grid.row(align=True)
        row.prop(prop, 'use_refraction_depth', text='', icon=get_hide_icon(prop.use_refraction_depth))
        row.prop(prop, 'new_refraction_depth', text='refraction depth', slider=True)

        row = grid.row(align=True)
        row.prop(prop, 'use_sss_translucency', text='', icon=get_hide_icon(prop.use_sss_translucency))
        row.prop(prop, 'new_sss_translucency', text='sss translucency')

        row = grid.row(align=True)
        row.prop(prop, 'use_pass_index', text='', icon=get_hide_icon(prop.use_pass_index))
        row.prop(prop, 'new_pass_index', text='pass index')

        # -----------------------------------------------------------------------------------------
        grid.separator()

        layout.label(text='Complete all operations with one click')
        layout.operator(OT_BatchSettingMmdMaterialProp.bl_idname)


@_add_cls
class OT_BatchSettingMmdMaterialProp(Operator):
    bl_idname = 'mte.batch_setting_mmd_material'
    bl_label = 'Batch update'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        mte_material_prop = scene.mte_material_prop
        material_func.batch_setting_mmd_material_prop(mte_material_prop)
        return {'FINISHED'}


@_add_cls
class MTE_Material_Panel_L2(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'MTE'
    bl_context = ''
    bl_idname = 'MTE_PT_Material_Panel_L2'
    # 菜单名字
    bl_label = 'Material Panel L2'

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        # -----------------------------------------------------------------------------------------
        layout.operator(OT_RemoveAllRedundantMmdShaderGroup.bl_idname)
        layout.operator(OT_CopyMaterialFromDataToObjectDialogOperator.bl_idname)
        layout.operator(OT_UserRemapMaterialFromDataToObjectDialogOperator.bl_idname)


@_add_cls
class OT_RemoveAllRedundantMmdShaderGroup(Operator):
    bl_idname = 'mte.remove_all_redundant_mmd_shader_group'
    bl_label = 'Remove all redundant mmd shader group'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        material_func.remove_all_redundant_mmd_shader_group()
        return {'FINISHED'}


@_add_cls
class OT_CopyMaterialFromDataToObjectDialogOperator(Operator):
    bl_idname = "object.copy_material_from_data_to_object_dialog"
    bl_label = "Copy Material From Data To Object Dialog"

    reverse_copy:   BoolProperty(name="Reverse copy", default=False)
    use_swap:       BoolProperty(name="Swap", default=False)
    use_ref:        BoolProperty(name="Reference", default=False)
    keep_slot_link: BoolProperty(name="Keep origin slot link", default=False)

    def execute(self, context):
        material_func.copy_material_from_data_to_object(
            self.reverse_copy, self.use_swap,
            self.use_ref, self.keep_slot_link
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


@_add_cls
class OT_UserRemapMaterialFromDataToObjectDialogOperator(Operator):
    bl_idname = "object.user_remap_material_from_data_to_object_dialog"
    bl_label = "User Remap Material From Data To Object Dialog"

    use_reverse:    BoolProperty(name="Reverse", default=False)

    def execute(self, context):
        material_func.user_remap_material_from_data_to_object(self.use_reverse)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)



# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)
    Scene.mte_material_prop = PointerProperty(type=MTE_Material_Prop)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
