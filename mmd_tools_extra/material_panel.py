import bpy
from bpy.types import PropertyGroup, Panel, Operator, Scene, UIList
from bpy.props import BoolProperty, IntProperty, FloatProperty, EnumProperty, FloatVectorProperty, StringProperty, PointerProperty, CollectionProperty

from fnmatch import fnmatch
from . import material_func
from .misc import alert_msg, _add_cls_ref, get_hide_icon
from mmd_tools.core import material as mmd_tool_material


class_list = []
_add_cls = _add_cls_ref(class_list)


@_add_cls
class MTE_Material_UL_Item_State(bpy.types.PropertyGroup):
    is_select: BoolProperty(default=False)
    material_name: StringProperty(default='')


@_add_cls
class MTE_Material_UL_Item(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index, flt_flag):
        icon = get_hide_icon(item.is_select)
        layout.prop(item, 'is_select', icon=icon, icon_only=True)
        layout.label(text=item.material_name, translate=False)


@_add_cls
class MTE_Material_Prop(PropertyGroup):

    selected_obj_mat_active:    IntProperty()
    selected_obj_mat_list:      CollectionProperty(type=MTE_Material_UL_Item_State)
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
    bl_options = {'DEFAULT_CLOSED'}
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

        # Check if the material list needs to be updated.
        _A = tuple(get_ul_mat_list())
        _B = tuple(get_selected_obj_mat_list())
        if _A != _B:
            row = grid.row(align=True)
            row.label(text='Outdated! Please refresh the material list.', icon='INFO')
        #

        row = grid.row(align=True).split(factor=0.8)
        row.template_list('MTE_Material_UL_Item', '', prop, 'selected_obj_mat_list', prop, 'selected_obj_mat_active', rows=4)

        col = row.column(align=True)
        col.operator(OT_MaterialListRefresh.bl_idname, text='Refresh', icon='FILE_REFRESH')
        col.separator()
        col.operator(OT_MaterialListSelect.bl_idname, text='Select All', icon='SELECT_EXTEND').select_type = 'SELECT_ALL'
        col.operator(OT_MaterialListSelect.bl_idname, text='Deselect All', icon='SELECT_SET').select_type = 'DESELECT_ALL'
        col.operator(OT_MaterialListSelect.bl_idname, text='Select Invert', icon='SELECT_SUBTRACT').select_type = 'SELECT_INVERT'

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


def get_selected_obj_mat_list():
    mat_list = []
    for mesh_obj in bpy.context.selected_objects:
        if mesh_obj.type != 'MESH':
            continue
        for slot in mesh_obj.material_slots:
            if slot.material is not None and slot.material.name not in mat_list and slot.material.library is None:
                mat_list.append(slot.material.name)
    return mat_list


def get_ul_mat_list():
    scene = bpy.context.scene
    prop = scene.mte_material_prop
    mat_list = []
    for item in prop.selected_obj_mat_list:
        mat_list.append(item.material_name)
    return mat_list


@_add_cls
class OT_MaterialListRefresh(Operator):
    bl_idname = 'mte.material_list_refresh'
    bl_label = 'Material list refresh'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        prop = scene.mte_material_prop
        
        new_mat_list = get_selected_obj_mat_list()
                    
        while len(prop.selected_obj_mat_list) < len(new_mat_list):
            prop.selected_obj_mat_list.add()

        need_del_ids = []
        for i, item in enumerate(prop.selected_obj_mat_list):
            if i < len(new_mat_list):
                if item.material_name != new_mat_list[i]:
                    item.material_name = new_mat_list[i]
                    item.is_select = False
            else:
                need_del_ids.append(i)
        need_del_ids = sorted(need_del_ids, reverse=True)
        for i in need_del_ids:
            prop.selected_obj_mat_list.remove(i)

        return {'FINISHED'}


@_add_cls
class OT_MaterialListSelect(Operator):
    bl_idname = 'mte.material_list_select'
    bl_label = 'Material list select'
    bl_options = {'REGISTER', 'UNDO'}

    select_type:   EnumProperty(
            default='SELECT_ALL', description='Select type',
            items=[('SELECT_ALL', 'SELECT_ALL', ''), ('DESELECT_ALL', 'DESELECT_ALL', ''), ('SELECT_INVERT', 'SELECT_INVERT', '')]
        )

    def execute(self, context):
        scene = context.scene
        prop = scene.mte_material_prop
        for item in prop.selected_obj_mat_list:
            if self.select_type == 'SELECT_ALL':
                item.is_select = True
            elif self.select_type == 'DESELECT_ALL':
                item.is_select = False
            elif self.select_type == 'SELECT_INVERT':
                item.is_select = not item.is_select
        return {'FINISHED'}


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
    bl_options = {'DEFAULT_CLOSED'}
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
        layout.operator(OT_CopyMaterialFromActivedToSelectedObjectDialog.bl_idname)
        layout.operator(OT_ReloadAllImage.bl_idname)
        layout.operator(OT_RemoveAllRedundantImage.bl_idname)


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


@_add_cls
class OT_CopyMaterialFromActivedToSelectedObjectDialog(Operator):
    bl_idname = 'mte.copy_material_from_actived_to_selected_object_dialog'
    bl_label = 'Copy Material From Actived To Selected Object Dialog'
    bl_options = {'REGISTER', 'UNDO'}

    only_active_slot:   BoolProperty(name="Only active material slot", default=False)
    use_ref:            BoolProperty(name="Reference", default=False)

    def execute(self, context):
        material_func.copy_material_from_active_to_select(
            only_active_slot=self.only_active_slot, use_ref=self.use_ref
        )
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


@_add_cls
class OT_ReloadAllImage(Operator):
    bl_idname = 'mte.reload_all_image'
    bl_label = 'Reload All Image'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        material_func.reload_all_image()
        return {'FINISHED'}


@_add_cls
class OT_RemoveAllRedundantImage(Operator):
    bl_idname = 'mte.remove_all_redundant_image'
    bl_label = 'Remove All Redundant Image'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        material_func.remove_all_redundant_image()
        return {'FINISHED'}


# -------------------------------------------------------------------------------


def register():
    for cls in class_list:
        bpy.utils.register_class(cls)
    Scene.mte_material_prop = PointerProperty(type=MTE_Material_Prop)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)
