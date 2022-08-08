
translation_dict = {
    'zh_CN': {
        # 通用
        ('*', 'Info'): '信息',
        ('*', 'Warning'): '警告',
        ('*', 'Error'): '错误',
        ('*', 'Success.'): '操作成功。',

        # bone_panel.py
        ('*', 'Bone Panel'): '骨骼面板',
        ('Operator', 'Clear selected bone roll'): '清除选择骨骼滚动角度',
        ('Operator', 'Symmetric selected bones X'): 'X轴镜像选中骨骼的设置',
        ('Operator', 'Auto setting and hide tip bone'): '自动设定和隐藏尖端骨骼',
        ('Operator', 'Select rigidbody by selected bone'): '基于已选择的骨骼选中关联的刚体',

        # bone_func.py
        ('*', 'This function can only be used in Armature Edit Mode.'): '只能在骨架编辑模式使用本功能。',
        ('*', 'This function can only be used in Pose Mode.'): '只能在姿态模式使用本功能。',
        ('*', 'This function can only be used in Pose Mode and Armature Edit Mode.'): '只能在姿态模式或骨架编辑模式使用本功能。',
        ('*', 'The actived object should be a valid armature object.'): '需要令骨架对象为激活对象。',
        ('*', 'Please select at least one bone.'): '请选中至少一根骨骼。',
        ('*', 'This function can only be used for armature of MMD model.'): '只能用于MMD模型的骨架。',
        ('*', 'Success. But the target bone is found to be among the selected bones, which may have unexpected results.'): '操作完成。但发现目标骨骼在选中的骨骼中，这可能产生意外的结果。',

        # material_panel.py
        ('*', 'patten'): '匹配材质名',
        ('*', 'jp_name'): '是否匹配日文名',
        
        ('*', 'diffuse'): '漫反射色',
        ('*', 'specular'): '高光色',
        ('*', 'ambient'): '环境色',
        ('*', 'alpha'): '透明度',
        ('*', 'shininess'): '高光系数',
        ('*', 'double side'): '双面',
        ('*', 'ground shadow'): '地面影',
        ('*', 'self shadow map'): '自阴影贴图',
        ('*', 'self shadow'): '自阴影',
        ('*', 'outline'): '边缘',
        ('*', 'outline color'): '边缘色',
        ('*', 'outline weight'): '边缘权重',
        ('*', 'base tex'): '基础贴图路径',
        ('*', 'sphere tex'): '球面贴图路径',
        ('*', 'sphere tex type'): '球面贴图类型',
        ('*', 'is shared toon tex'): '是否使用共享toon贴图',
        ('*', 'shared toon tex id'): '共享toon贴图序号',
        ('*', 'toon tex'): 'toon贴图路径',

        ('*', 'delimiter str'): '分隔符',
        ('*', 'alert_name_j'): '是否修改日文名',
        ('*', 'del prefix'): '是否删除前缀',
        ('*', 'del suffix'): '是否删除后缀',
        ('*', 'new prefix'): '增加前缀',
        ('*', 'new suffix'): '增加后缀',

        ('*', 'replace str'): '材质名替换',
        ('*', 'old str'): '被替换的文本',
        ('*', 'new str'): '替换后的文本',

        ('*', 'backface culling'): '背面剔除',
        ('*', 'blend method'): '混合模式',
        ('*', 'shadow method'): '阴影模式',
        ('*', 'alpha threshold'): '钳制阈值',
        ('*', 'screen refraction'): '屏幕空间折射',
        ('*', 'refraction depth'): '折射深度',
        ('*', 'sss translucency'): '次表面半透明',
        ('*', 'pass index'): '通道编号',

        ('*', 'Complete all operations with one click'): '一键完成所有修改操作',

        ('*', 'Material Panel'): '材质面板',
        ('*', 'Batch alter material props.'): '批量修改材质属性',
        ('Operator', 'Batch update'): '批量修改',

        ('*', 'Material Panel L2'): '材质面板2',
        ('Operator', 'Remove all redundant mmd shader group'): '删除所有冗余的MMDShader组',


        # material_func.py
        ('*', 'Please select at least one mesh object.'): '请选中至少一个网格对象。',
        ('*', 'No MMD materials were found in the selected mesh object.'): '在选择的网格对象中没有发现任何MMD材质。',


        # action_panel.py
        ('*', 'Action Panel'): '动作面板',
        ('Operator', 'Fast Bake Action Dialog'): '快速烘焙对话框',
        ('*', 'Action name'): '动作名',
        ('*', 'Frame start'): '起始帧',
        ('*', 'Frame end'): '结束帧',
        ('*', 'Frame step'): '帧步长',
        ('*', 'No scale'): '不使用缩放帧',
        ('*', 'Override existing action'): '覆盖已有动作',
        ('*', 'Disable constraints after baking'): '烘焙完成后禁用约束',
        ('*', 'Clean eps'): '清除阈值',
        ('*', 'Max clean cycle'): '最多重复清理次数',
        ('*', 'Clean redundant frame'): '清理冗余帧',
        ('*', 'Active action'): '激活为当前动作',
        ('Operator', 'Clean Action Dialog'): '清理动作对话框',


        # action_func.py
        ('*', 'No found any active action on actived armature.'): '目标骨架发现没有激活的动画对象。',


        # morph_panel.py
        ('*', 'Morph Panel'): '变形面板',
        ('Operator', 'Replace Material Morph Related Mesh Dialog'): '材质变形相关网格替换对话框',
        ('*', 'old mesh name patten'): '待替换网格名，支持通配符',
        ('*', 'new mesh name'): '新网格名',


        # morph_func.py
        ('*', 'The actived object should be a valid mmd root object.'): '需要令mmd_root对象为激活对象。',


        # rigidbody_panel.py
        ('*', 'Rigidbody Panel'): '刚体面板',
        ('Operator', 'Select all non bone ref rigid'): '选择所有没有引用任何骨骼的刚体',
        ('Operator', 'Auto rename selected rigidbody'): '自动重命名选择的刚体',
        ('Operator', 'Select joint by selected rigidbody'): '基于已选择的刚体选择关联的约束点(J点)',
        ('Operator', 'Select bone by selected rigidbody'): '基于已选择的刚体选择关联的骨骼',


        # rigidbody_func.py
        ('*', 'This function can only be used in Object Mode.'): '只能在物体模式使用本功能。',
        ('*', 'Please select at least one MMD rigidbody.'): '请至少选中一个MMD刚体。',
        ('*', 'The MMD root object associated with the MMD rigidbody does not exist.'): 'MMD刚体关联的MMD根对象不存在。',
        ('*', 'The MMD armature object associated with the MMD rigidbody does not exist.'): 'MMD刚体关联的MMD骨架对象不存在。',
        

        # joint_panel.py
        ('*', 'Joint Panel'): '约束点（J点）面板',
        ('Operator', 'Select all invalid joint'): '选择所有无效约束点',
        ('Operator', 'Auto Rename selected joint'): '自动重命名已选择的约束点',
        ('Operator', 'Select rigidbody by selected joint'): '选择刚体基于已选择的约束点',
        
        
        # joint_func.py
        ('*', 'Please select at least one MMD joint.'): '请至少选中一个MMD约束点。',
        
        
        # other_panel.py
        ('*', 'Other Panel'): '其他面板',
        ('Operator', 'Delete all vrm obj'): '删除所有VRM对象',
        ('Operator', 'Delete all invalid driver'): '删除所有无效驱动器',
        ('Operator', 'Delete all ghost object'): '删除所有幽灵对象',
        

        # other_func.py

    },
}
