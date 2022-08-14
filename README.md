# blender_mmd_tools_extra

This is an enhancement tool for blender_mmd_tools.  
Welcom issue, function and translations pr.  

这是一个 blender_mmd_tools 的增强工具。  
欢迎提出问题和贡献新的功能和翻译。  

Depends on blender_mmd_tools  
Minimum Blender Supported Version is 3.0  
Recommended Blender version 3.2.2 or newer  

依赖于 blender_mmd_tools  
最低 Blender 支持版本 Blender 3.0  
建议 Blender 版本 3.2.2 或更新  

blender_mmd_tools Link: https://github.com/UuuNyaa/blender_mmd_tools/tree/main


# Features / 功能介绍

----------------------------------------------------------------------
## Bone Panel / 骨骼面板

### Clear selected bone roll / 清除选择骨骼滚动角度
Armature Edit Mode. Requires at least one bone to be selected.  
骨架编辑模式，需要选中至少一根骨骼。  

### Symmetric selected bones X / X轴镜像选中骨骼的设置
Armature Edit Mode. Requires at least one bone to be selected.  
It not only includes basic Blender attributes such as bone position and posture, but also includes mmd_bone name, fixed axis and other mmd attributes.  
骨架编辑模式，需要选中至少一根骨骼。  
不仅包括骨骼位置，姿态等基础Blender属性，还包括mmd_bone的名字，固定轴等mmd属性。  

### Auto setting and hide tip bone / 自动设定和隐藏尖端骨骼
Pose Mode. Requires at least one bone to be selected.  
Automatically hides bones that meet the following conditions:  
1. The last character of a Japanese name is "先"  
2. The bone has setting with is_tip  

姿态模式，需要选中至少一根骨骼。  
自动隐藏符合以下条件的骨骼：  
1. 日文名最后一个字是 "先"
2. 已设定尖端骨骼的骨骼  

### Select rigidbody by selected bone / 基于已选择的骨骼选中关联的刚体
Armature Edit Mode or Pose Mode. Requires at least one bone to be selected.  
骨架编辑模式或姿态模式，需要选中至少一根骨骼。  

### Disconnect all physical bone / 断离所有物理骨骼
Armature Edit Mode.  
After the physical bone is disconnect, it will be free to move. Then store the original connection settings in the mmd_bone_use_connect attribute.  
This function is generally used in skeletal animations baked into physics.  
骨架编辑模式。  
物理骨骼断离后，将可以自由移动。然后把原来的连接设定储存在 mmd_bone_use_connect 属性内。  
本功能一般用于物理烘焙到的骨骼动画中。  

Example/示例：https://www.bilibili.com/video/BV1ga411Z7aJ

### Cancel disconnect all physical bone / 取消断离所有物理骨骼
Armature Edit Mode.  
Restores the original connection settings of the physical bones.  
骨架编辑模式。  
恢复物理骨骼原来的连接设定。  

----------------------------------------------------------------------
## Material Panel / 材质面板

### Batch update / 批量修改
Any mode.  
Modify material properties in batches according to the material name patten.  
任意模式。  
根据材质名匹配表达式，批量修改属性。  

----------------------------------------------------------------------
## Material Panel 2 / 材质面板2

### Remove all redundant mmd shader group / 删除所有冗余的MMDShader组
Any mode.  
Remove all MMDShaderDev.XXX and MMDTexUV.XXX and migrate to MMDShaderDev and MMDTexUV.  
任意模式。  
移除所有的 MMDShaderDev.XXX 和 MMDTexUV.XXX，并迁移为 MMDShaderDev 和 MMDTexUV。  

----------------------------------------------------------------------
## Morph Panel / 变形面板

### Replace Material Morph Related Mesh Dialog / 材质变形相关网格替换对话框
Any mode.  
Used to batch replace the related_mesh of material morph.  
任意模式。  
用于批量修改材质变形的相关网格。  

----------------------------------------------------------------------
## Rigidbody Panel / 刚体面板

### Select all non bone ref rigid / 选择所有没有引用任何骨骼的刚体
Object Mode.  
物体模式。  

### Auto rename selected rigidbody / 自动重命名选择的刚体
Object Mode. Requires at least one rigidbody to be selected.  
物体模式，需要选中至少一个刚体对象。  

Example/示例：78.rigid.ひざ.L  

### Select joint by selected rigidbody / 基于已选择的刚体选择关联的约束点(J点)
Object Mode. Requires at least one rigidbody to be selected.  
物体模式，需要选中至少一个刚体对象。  

### Select bone by selected rigidbody / 基于已选择的刚体选择关联的骨骼
Object Mode. Requires at least one rigidbody to be selected.  
物体模式，需要选中至少一个刚体对象。  


----------------------------------------------------------------------
## Joint Panel / 约束点（J点）面板

### Select all invalid joint / 选择所有无效约束点
Object Mode.  
物体模式。  

### Auto Rename selected joint / 自动重命名已选择的约束点
Object Mode. Requires at least one rigidbody to be selected.  
物体模式。需要选中至少一个约束点对象。  

Example/示例：280.joint.ひじ.L->袖_0_1.L  

### Select rigidbody by selected joint / 基于已选择的约束点选择刚体
Object Mode. Requires at least one rigidbody to be selected.  
物体模式。需要选中至少一个约束点对象。  


----------------------------------------------------------------------
## Action Panel / 动作面板

### Fast Bake Action Dialog / 快速烘焙对话框
Armature Edit Mode or Pose Mode. Requires at least one bone to be selected.  
The visual transformation baking function I implemented currently only supports baking skeletal animations, which can be 100 times faster than the official baking function.  
骨架编辑模式或姿态模式，需要选中至少一根骨骼。  
我实现的可视变换烘焙功能，目前只支持烘焙骨骼动画，相比官方的烘焙功能，可以快100倍。  

Example/示例：https://www.bilibili.com/video/BV1ga411Z7aJ

### Clean Action Dialog / 清理动作对话框
Armature Edit Mode or Pose Mode. Requires at least one bone to be selected.  
I implement the action cleanup function, and currently only support cleanup skeleton animations.  
Because the official action cleanup function cannot be called in python, I wrote an action cleanup function.  
骨架编辑模式或姿态模式，需要选中至少一根骨骼。  
我实现动作清理功能，目前只支持清理骨骼动画。  
因为官方的动作清理功能无法在python中调用，所以我编写了一个动作清理功能。  

----------------------------------------------------------------------
## Other Panel / 其他面板

### Delete all vrm obj / 删除所有VRM对象
Any mode.  
Once the VRM plugin is enabled, a large number of invisible and useless objects starting with '| vrm' will be automatically left behind.  
This function can delete all objects starting with '| vrm' with one click.  
任意模式。  
一旦启用VRM插件，将会在自动遗留大量的不可见的无用的 '| vrm' 开头的物体对象。  
本功能可以一键删除所有以 '| vrm' 开头的物体对象。  

### Delete all invalid driver / 删除所有无效驱动器
Any mode.  
任意模式。  

### Delete all ghost object / 删除所有幽灵对象
Any mode.  
All objects that do not belong to any scene and view layers will be deleted.  
任意模式。  
将会全部删除不属于任何场景和视图层的物体对象。  

----------------------------------------------------------------------
