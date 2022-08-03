import bpy
from mathutils import Matrix, Quaternion, Vector


def _add_cls_ref(ls):
    def _add_cls(cls):
        ls.append(cls)
        return cls
    return _add_cls


def alert_msg(title, message):
    print(f'{title}: {message}')
    def draw(self, context):
        self.layout.label(text=str(message))
    bpy.context.window_manager.popup_menu(draw, title=title, icon='CUBE')


def get_hide_icon(enabled):
    if enabled:
        return 'HIDE_OFF'
    else:
        return 'HIDE_ON'


def filter_mmd_rigidbody(objs):
    keep = []
    for obj in objs:
        if obj.rigid_body is not None and\
            hasattr(obj, 'mmd_rigid') and\
            obj.mmd_rigid is not None:
            keep.append(obj)
    return keep


def filter_mmd_joint(objs):
    keep = []
    for obj in objs:
        if obj.rigid_body_constraint is not None and \
            hasattr(obj, 'mmd_joint') and\
            obj.mmd_joint is not None:
            keep.append(obj)
    return keep
