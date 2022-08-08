import bpy
import fnmatch
from .misc import alert_msg


def replace_material_morph_related_mesh(old_related_mesh_patten, new_related_mesh):
    obj = bpy.context.active_object
    if obj is None or obj.mmd_type != 'ROOT':
        alert_msg('Error', 'The actived object should be a valid mmd root object.')
        return

    root_obj = obj
    for mm in root_obj.mmd_root.material_morphs:
        for data in mm.data:
            if fnmatch.fnmatch(data.related_mesh, old_related_mesh_patten):
                data.related_mesh = new_related_mesh

    alert_msg('Info', 'Success.')
