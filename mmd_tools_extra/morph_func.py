import bpy
import fnmatch
from .misc import alert_msg


def replace_material_morph_related_mesh(old_related_mesh_patten, new_related_mesh):
    obj = bpy.context.active_object
    if obj is None or obj.mmd_type != 'ROOT':
        alert_msg('错误', '需要令mmd_root对象为激活对象。')
        return

    root_obj = obj
    for mm in root_obj.mmd_root.material_morphs:
        for data in mm.data:
            if fnmatch.fnmatch(data.related_mesh, old_related_mesh_patten):
                data.related_mesh = new_related_mesh

    alert_msg('信息', '操作完成')
