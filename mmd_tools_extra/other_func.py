import bpy
from .misc import alert_msg


def delete_all_vrm_obj():
    need_del_obj = []

    for obj in bpy.data.objects:
        if obj.name.startswith('￤VrmAddon'):
            need_del_obj.append(obj)

    for obj in need_del_obj:
        print('Del', obj.name)
        bpy.data.objects.remove(obj)

    alert_msg('Info', 'Success.')


def delete_all_invalid_driver():
    for obj in bpy.data.objects:
        if obj.animation_data is not None:
            for dr in obj.animation_data.drivers:
                if not dr.is_valid:
                    print(f'Del {dr.data_path}')
                    obj.driver_remove(dr.data_path, -1)

        if obj.data is not None and obj.data.animation_data is not None:
            for dr in obj.data.animation_data.drivers:
                if not dr.is_valid:
                    print(f'Del {dr.data_path}')
                    obj.data.driver_remove(dr.data_path, -1)

    alert_msg('Info', 'Success.')


def delete_all_ghost_object():
    all_scene_obj_set = set()
    for scene in bpy.data.scenes:
        all_scene_obj_set.update(scene.objects)

    for obj_i in range(len(bpy.data.objects))[::-1]:
        obj = bpy.data.objects[obj_i]
        if obj not in all_scene_obj_set:
            print(f'Del {obj.name}')
            bpy.data.objects.remove(obj)

    alert_msg('Info', 'Success.')
