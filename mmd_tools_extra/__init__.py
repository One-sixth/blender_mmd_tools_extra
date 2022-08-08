bl_info = {
    "name": "mmd_tool_extra",           #插件名字
    "author": "onesixth",               #作者名字
    "version": (0, 0, 1),               #插件版本
    "blender": (3, 0, 0),               #需要的*最低* blender 版本
    "location": "3DView > Tools",       #插件所在位置
    "description": "用于mmd_tool扩展",  #描述
    "support": 'COMMUNITY',             #支持等级（社区支持）
    "category": "Tool",                 #分类
    #"warning": "",
}

import bpy
from bpy.types import Operator
from bpy.props import BoolProperty

from . import bone_panel
from . import material_panel
from . import morph_panel
from . import rigidbody_panel
from . import joint_panel
from . import action_panel
from . import other_panel
from .m17n import translation_dict


panel_cls = [bone_panel, material_panel, morph_panel, rigidbody_panel, joint_panel, action_panel, other_panel]


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
