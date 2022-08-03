import bpy
import fnmatch
from .misc import alert_msg
from mmd_tools.core.material import FnMaterial


def batch_setting_mmd_material_prop(mte_material_prop):

    mesh_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

    if len(mesh_objs) == 0:
        alert_msg('信息', '请选中至少一个网格对象')
        return

    prop = mte_material_prop

    mats = []

    for obj in mesh_objs:
        for i in range(len(obj.material_slots)):
            # 材质槽是不可修改的，必须使用名字获得真正的材质对象
            mat = bpy.data.materials[obj.material_slots[i].name]

            # 目标材质必须有mmd_material属性
            if hasattr(mat, 'mmd_material') and mat.mmd_material is not None:
                if prop.match_name_j:
                    b = fnmatch.fnmatch(mat.mmd_material.name_j, prop.match_material_name)
                else:
                    b = fnmatch.fnmatch(mat.name, prop.match_material_name)
                if b:
                    mats.append(mat)
    
    if len(mesh_objs) == 0:
        alert_msg('信息', '在选择的网格对象中没有发现任何MMD材质')
        return

    for mat in mats:
        fn_mat = FnMaterial(mat)

        if prop.use_diffuse_color:
            mat.mmd_material.diffuse_color = prop.new_diffuse_color
            
        if prop.use_specular_color:
            mat.mmd_material.specular_color = prop.new_specular_color

        if prop.use_ambient_color:
            mat.mmd_material.ambient_color = prop.new_ambient_color

        if prop.use_alpha:
            mat.mmd_material.alpha = prop.new_alpha

        if prop.use_shininess:
            mat.mmd_material.shininess = prop.new_shininess
            
        if prop.use_double_side:
            mat.mmd_material.is_double_sided = prop.new_double_side
            
        if prop.use_ground_shadow:
            mat.mmd_material.enabled_drop_shadow = prop.new_ground_shadow
            
        if prop.use_self_shadow_map:
            mat.mmd_material.enabled_self_shadow_map = prop.new_self_shadow_map
            
        if prop.use_self_shadow:
            mat.mmd_material.enabled_self_shadow = prop.new_self_shadow
            
        if prop.use_outline:
            mat.mmd_material.enabled_toon_edge = prop.new_edge
            
        if prop.use_outline_color:
            mat.mmd_material.edge_color = prop.new_outline_color
            
        if prop.use_outline_weight:
            mat.mmd_material.edge_weight = prop.new_outline_weight
        
        if prop.use_base_tex:
            fn_mat.create_texture(prop.new_base_tex)

        if prop.use_sphere_tex:
            fn_mat.create_sphere_texture(prop.new_sphere_tex)

        if prop.use_sphere_tex_type:
            mat.mmd_material.sphere_texture_type = prop.new_sphere_tex_type
            fn_mat.update_sphere_texture_type()
        
        if prop.use_is_shared_toon_tex:
            mat.mmd_material.is_shared_toon_texture = prop.new_is_shared_toon_tex

        if prop.use_shared_toon_tex_id:
            mat.mmd_material.shared_toon_texture = prop.new_shared_toon_tex_id

        if prop.use_toon_tex:
            mat.mmd_material.toon_texture = prop.new_toon_tex
        
        # -------------------------------------------------------------------------------------
        
        if prop.use_del_prefix and prop.delimiter_str != '':
            if prop.use_alert_name_j:
                ns = mat.mmd_material.name_j.split(prop.delimiter_str)
                if len(ns) > 1:
                    mat.mmd_material.name_j = prop.delimiter_str.join(ns[1:])
            else:
                ns = mat.name.split(prop.delimiter_str)
                if len(ns) > 1:
                    mat.name = prop.delimiter_str.join(ns[1:])

        if prop.use_del_suffix and prop.delimiter_str != '':
            if prop.use_alert_name_j:
                ns = mat.mmd_material.name_j.split(prop.delimiter_str)
                if len(ns) > 1:
                    mat.mmd_material.name_j = prop.delimiter_str.join(ns[:-1])
            else:
                ns = mat.name.split(prop.delimiter_str)
                if len(ns) > 1:
                    mat.name = prop.delimiter_str.join(ns[:-1])
        
        if prop.use_add_prefix:
            if prop.use_alert_name_j:
                mat.mmd_material.name_j = prop.new_add_prefix + prop.delimiter_str + mat.mmd_material.name_j
            else:
                mat.name = prop.new_add_prefix + prop.delimiter_str + mat.name
        
        if prop.use_add_suffix:
            if prop.use_alert_name_j:
                mat.mmd_material.name_j = mat.mmd_material.name_j + prop.delimiter_str + prop.new_add_suffix
            else:
                mat.name = mat.name + prop.delimiter_str + prop.new_add_suffix

        if prop.use_replace_str:
            if prop.use_alert_name_j:
                mat.mmd_material.name_j = mat.mmd_material.name_j.replace(prop.old_replace_str, prop.new_replace_str)
            else:
                mat.name = mat.name.replace(prop.old_replace_str, prop.new_replace_str)
        
        # -------------------------------------------------------------------------------------

        if prop.use_backface_culling:
            mat.use_backface_culling = prop.new_backface_culling
        
        if prop.use_blend_method:
            mat.blend_method = prop.new_blend_method
        
        if prop.use_shadow_method:
            mat.shadow_method = prop.new_shadow_method
        
        if prop.use_alpha_threshold:
            mat.alpha_threshold = prop.new_alpha_threshold
        
        if prop.use_screen_refraction:
            mat.use_screen_refraction = prop.new_screen_refraction
        
        if prop.use_refraction_depth:
            mat.refraction_depth = prop.new_refraction_depth
        
        if prop.use_sss_translucency:
            mat.use_sss_translucency = prop.new_sss_translucency
                
        if prop.use_pass_index:
            mat.pass_index = prop.new_pass_index
    
        # -------------------------------------------------------------------------------------

    alert_msg('信息', f'更新了{len(mats)}个材质')
    

def remove_all_redundant_mmd_shader_group():
    mesh_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

    if len(mesh_objs) == 0:
        alert_msg('信息', '请选中至少一个网格对象')
        return

    mats = []

    for obj in mesh_objs:
        for i in range(len(obj.material_slots)):
            # 材质槽是不可修改的，必须使用名字获得真正的材质对象
            mat = bpy.data.materials[obj.material_slots[i].name]

            # 目标材质必须有mmd_material属性，必须启用节点组
            if hasattr(mat, 'mmd_material') and mat.mmd_material is not None and mat.use_nodes:
                mats.append(mat)
    
    if len(mesh_objs) == 0:
        alert_msg('信息', '在选择的网格对象中没有发现任何MMD材质')
        return
    
    def replace_node_group(node_group_name, node_name):
        # 寻找 MMDShaderDev 着色器组
        mmd_shader_group = bpy.data.node_groups.get(node_group_name)
        if mmd_shader_group is None:
            for ng in bpy.data.node_groups:
                if ng.name.startswith(node_group_name + '.'):
                    ng.name = node_group_name
                    mmd_shader_group = ng
                    break
        
        if mmd_shader_group is None:
            alert_msg('信息', f'没有发现任何{node_group_name}节点组')
            return
        
        for mat in mats:
            n = mat.node_tree.nodes.get(node_name)
            if n is not None:
                n.node_tree = mmd_shader_group
    
    # 寻找 MMDShaderDev 着色器组
    replace_node_group('MMDShaderDev', 'mmd_shader')
    replace_node_group('MMDTexUV', 'mmd_tex_uv')
    
    alert_msg('信息', '操作完成')
