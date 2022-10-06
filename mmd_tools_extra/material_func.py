from unicodedata import name
import bpy
import fnmatch
from .misc import alert_msg, find_mmd_root_obj
from mmd_tools.core.material import FnMaterial


def batch_setting_mmd_material_prop(mte_material_prop):
    mesh_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

    if len(mesh_objs) == 0:
        alert_msg('Info', 'Please select at least one mesh object.')
        return

    prop = mte_material_prop

    mats = []

    for obj in mesh_objs:
        for i in range(len(obj.material_slots)):
            # 材质槽是不可修改的，必须获得真正的材质对象
            mat = obj.material_slots[i].material
            if mat is None:
                continue

            # 目标材质必须有mmd_material属性
            if hasattr(mat, 'mmd_material') and mat.mmd_material is not None:
                if prop.match_name_j:
                    b = fnmatch.fnmatch(mat.mmd_material.name_j, prop.match_material_name)
                else:
                    b = fnmatch.fnmatch(mat.name, prop.match_material_name)
                if b:
                    mats.append(mat)
    
    if len(mesh_objs) == 0:
        alert_msg('Info', 'No MMD materials were found in the selected mesh object.')
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

    print(f'Updated {len(mats)} materials.')
    alert_msg('Info', 'Success.')
    

def remove_all_redundant_mmd_shader_group():
    mesh_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

    if len(mesh_objs) == 0:
        alert_msg('Info', 'Please select at least one mesh object.')
        return

    mats = []
    for obj in mesh_objs:
        for i in range(len(obj.material_slots)):
            # 材质槽是不可修改的，必须获得真正的材质对象
            mat = obj.material_slots[i].material
            if mat is None:
                continue

            # 目标材质必须有mmd_material属性，必须启用节点组
            if hasattr(mat, 'mmd_material') and mat.mmd_material is not None and mat.use_nodes:
                mats.append(mat)
    
    if len(mesh_objs) == 0:
        alert_msg('Info', 'No MMD materials were found in the selected mesh object.')
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
            print('No shader_node groups found with name {node_group_name}')
            return
        
        for mat in mats:
            n = mat.node_tree.nodes.get(node_name)
            if n is not None:
                n.node_tree = mmd_shader_group
    
    # 寻找 MMDShaderDev 着色器组
    replace_node_group('MMDShaderDev', 'mmd_shader')
    replace_node_group('MMDTexUV', 'mmd_tex_uv')
    
    alert_msg('Info', 'Success.')


def copy_material_from_data_to_object(reverse_copy, use_swap, use_ref, keep_slot_link):
    objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

    if len(objs) == 0:
        alert_msg('Info', 'Please select at least one mesh object.')
        return

    for obj in objs:
        for slot in obj.material_slots:
            ori_slot_link = slot.link

            if not reverse_copy:
                slot.link = 'DATA'
                mat = slot.material
                if not use_ref and mat is not None:
                    mat = mat.copy()

                slot.link = 'OBJECT'
                mat2 = slot.material
                slot.material = mat

                if use_swap:
                    slot.link = 'DATA'
                    slot.material = mat2
                
                if keep_slot_link:
                    slot.link = ori_slot_link
                else:
                    slot.link = 'OBJECT'

            else:
                slot.link = 'OBJECT'
                mat = slot.material
                if not use_ref and mat is not None:
                    mat = mat.copy()

                slot.link = 'DATA'
                mat2 = slot.material
                slot.material = mat

                if use_swap:
                    slot.link = 'OBJECT'
                    slot.material = mat2
                
                if keep_slot_link:
                    slot.link = ori_slot_link
                else:
                    slot.link = 'DATA'

    alert_msg('Info', 'Success.')


def user_remap_material_from_data_to_object(use_reverse):
    objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

    if len(objs) == 0:
        alert_msg('Info', 'Please select at least one mesh object.')
        return

    for obj in objs:
        for slot in obj.material_slots:
            ori_slot_link = slot.link

            slot.link = 'OBJECT'
            obj_mat = slot.material
            slot.link = 'DATA'
            data_mat = slot.material

            if obj_mat is not None and data_mat is not None:
                if not use_reverse:
                    data_mat.user_remap(obj_mat)
                else:
                    obj_mat.user_remap(data_mat)
            
            slot.link = ori_slot_link

    alert_msg('Info', 'Success.')


def copy_material_from_active_to_select(only_active_slot, use_ref):
    active_obj = bpy.context.active_object
    select_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
    
    if active_obj is None or active_obj.type != 'MESH':
        alert_msg('Error!', 'The actived object should be a valid mesh object.')
        return

    if active_obj in select_objs:
        select_objs.remove(active_obj)
    
    if len(select_objs) == 0:
        alert_msg('Error!', 'At least one other mesh object needs to be selected in addition to the active object.')
        return

    def ensure_enough_slots(obj, n_slot):
        while len(obj.material_slots) < n_slot:
            obj.data.materials.append(None)
    
    def update_mmd_material_morph_ref(obj, old_mat, new_mat):
        if old_mat is None:
            return
        root_obj = find_mmd_root_obj(obj)
        if root_obj is None:
            return
        for mat_morph in root_obj.mmd_root.material_morphs:
            for mat_morph_item in mat_morph.data:
                if mat_morph_item.material == old_mat.name:
                    mat_morph_item.material = new_mat.name
    
    for obj in select_objs:
        if only_active_slot:
            old_mat = obj.active_material
            new_mat = active_obj.active_material if use_ref else active_obj.active_material.copy()

            update_mmd_material_morph_ref(obj, old_mat, new_mat)
            obj.active_material = new_mat

        else:
            ensure_enough_slots(obj, len(active_obj.material_slots))
            for m_i, m in enumerate(active_obj.data.materials):
                old_mat = obj.data.materials[m_i]
                new_mat = m if use_ref else m.copy()

                update_mmd_material_morph_ref(obj, old_mat, new_mat)
                obj.data.materials[m_i] = new_mat
    
    alert_msg('Info', 'Success.')
