bl_info = {
    "name": "mmd_tools_extra",
    "author": "onesixth",
    "version": (0, 0, 2),
    "blender": (3, 2, 0),
    "location": "3DView > Tools",
    "description": "Extra functionality for blender_mmd_tools.",
    "support": 'COMMUNITY',
    "category": "Tool",
    "wiki_url": "https://github.com/One-sixth/blender_mmd_tools_extra/tree/main",
    #"warning": "",
}

import bpy

from . import bone_panel
from . import material_panel
from . import morph_panel
from . import rigidbody_panel
from . import joint_panel
from . import action_panel
from . import other_panel
from . import override_library_panel
from .m17n import translation_dict


panel_cls = [bone_panel, material_panel, morph_panel, rigidbody_panel, joint_panel, action_panel, other_panel, override_library_panel]


def register():
    #启用插件时候执行
    print('register mmd_tools_extra')

    # 注册翻译
    bpy.app.translations.register(bl_info['name'], translation_dict)
    # 注册面板
    for panel in panel_cls:
        panel.register()


def unregister():
    #关闭插件时候执行
    print('unregister mmd_tools_extra')
    # 卸载面板
    for panel in panel_cls:
        panel.unregister()
    # 卸载翻译
    bpy.app.translations.unregister(bl_info['name'])
