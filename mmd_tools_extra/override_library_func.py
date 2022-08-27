import bpy
from .misc import alert_msg


def sorted_objs_from_top_to_bottom(objs):
    def find_root(obj):
        while obj.parent is not None:
            obj = obj.parent
        return obj
    
    def gen_obj_tree_top2bottom(obj):
        o_list = []
        child = [obj]
        while len(child) > 0:
            item = child.pop(0)
            o_list.append(item)
            # print(item.name)
            child.extend(item.children)
        return o_list
    
    sorted_objs = []
    for obj in objs:
        if obj in sorted_objs:
            continue
        root = find_root(obj)
        o_list = gen_obj_tree_top2bottom(root)
        assert obj in o_list
        sorted_objs.extend(o_list)

    obj_ids = [sorted_objs.index(obj) for obj in objs]
    sorted_objs2 = sorted(zip(objs, obj_ids), key=lambda x: x[1])
    sorted_objs2 = [a[0] for a in sorted_objs2]
    return sorted_objs2


def batch_create_override_library(
        make_local,
        recusive_children,
        include_mesh, include_mesh_data, include_material,
        include_armature, include_armature_data,
        include_empty,
        include_camera, include_camera_data,
    ):
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
    if bpy.context.mode not in ['OBJECT']:
        alert_msg('Error', 'This function can only be used in Object Mode.')
        return

    objs = list(bpy.context.selected_objects)
    if len(objs) == 0:
        alert_msg('Error', 'Please select at least one object.')
        return
    
    cur_scene = bpy.context.scene
    cur_viewlayer = bpy.context.view_layer

    # 用于恢复层级结构
    parent_tree = {}
    child_tree = {}
    new_name_map = {}

    if recusive_children:
        child_objs = []
        for obj in objs:
            child_objs.extend(obj.children_recursive)
        objs = list(set(objs + child_objs))
    
    # 返回的是从顶到底的顺序，需要的是从底到顶的顺序
    objs = sorted_objs_from_top_to_bottom(objs)[::-1]
    
    collects = []
    for obj in objs:
        collects.extend(obj.users_collection)
    collects = list(set(collects))
    
    def do_create_override(d):
        if hasattr(d, 'type'):
            # OBJECT
            if make_local:
                # TODO 功能不完善，一些object无法通过python api来转换
                # 只能使用大纲进行转换
                bpy.ops.object.select_all(action='DESELECT')
                is_hide = d.hide_get()
                is_hide_select = d.hide_select
                d.hide_set(False)
                d.hide_select = False
                d.select_set(True)
                bpy.context.view_layer.update()
                bpy.ops.object.make_local()
                d.hide_set(is_hide)
                d.hide_select = is_hide_select
            else:
                # if d.parent is not None and d.parent.library is not None:
                #     # 必须要递归生成库覆盖
                #     do_create_override(d.parent)
                if d.library is not None:
                    # 后面我发现，只要使用逆序生成，就能尽可能保持结构
                    # ori_parent = d.parent
                    d.override_create(remap_local_usages=True)
                    # d.parent = ori_parent
                    # cur_viewlayer.objects.active = d
                    # bpy.ops.object.make_override_library()
        else:
            # DATA
            if make_local:
                d.make_local()
            else:
                if d.library is not None:
                    d.override_create(remap_local_usages=True)
    
    # 本函数有bug，需要至少到 blender 3.3 stable 发布后才能使用
    # def do_create_override(d):
        # if make_local:
        #     d.make_local()
        # else
    #         d.override_hierarchy_create(cur_scene, cur_viewlayer)
    
    for collect in collects:
        do_create_override(collect)

    for obj in objs:
        if obj.type == 'MESH':
            if include_mesh:
                do_create_override(obj)
            if include_mesh_data:
                do_create_override(obj.data)
            if include_material:
                mats = [slot.material for slot in obj.material_slots if slot.material is not None]
                for mat in mats:
                    do_create_override(mat)
        
        if obj.type == 'ARMATURE':
            if include_armature:
                do_create_override(obj)
            if include_armature_data:
                do_create_override(obj.data)
        
        if obj.type == 'EMPTY':
            if include_empty:
                do_create_override(obj)
        
        if obj.type == 'CAMERA':
            if include_camera:
                do_create_override(obj)
            if include_camera_data:
                do_create_override(obj.data)

    alert_msg('Info', 'Success.')
