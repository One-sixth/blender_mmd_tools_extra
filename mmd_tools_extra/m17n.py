
translation_dict = {

    # ------------------------------------------------------------------------------------------------------------
    'zh_CN': {
        # common
        ('*', 'Info'): '信息',
        ('*', 'Warning'): '警告',
        ('*', 'Error'): '错误',
        ('*', 'Success.'): '操作成功。',

        # bone_panel.py
        ('*', 'Bone Panel'): '骨骼面板',
        ('Operator', 'Clear selected bone roll'): '清除选择骨骼滚动角度',
        ('Operator', 'Symmetric selected bones X'): 'X轴镜像选中骨骼的设置',
        ('Operator', 'Auto setting and hide tip bone'): '自动设定和隐藏尖端骨骼',
        ('Operator', 'Hide all uncontrollable bone'): '隐藏所有不可控制骨骼',
        ('Operator', 'Hide all physics bone'): '隐藏所有物理骨骼',
        ('*', 'Pose mode'): '姿态模式',
        ('Operator', 'Select rigidbody by selected bone'): '基于已选择的骨骼选中关联的刚体',
        ('Operator', 'Disconnect all physical bone'): '断离所有物理骨骼',
        ('Operator', 'Cancel disconnect all physical bone'): '取消断离所有物理骨骼',

        # bone_func.py
        ('*', 'This function can only be used in Armature Edit Mode.'): '只能在骨架编辑模式使用本功能。',
        ('*', 'This function can only be used in Pose Mode.'): '只能在姿态模式使用本功能。',
        ('*', 'This function can only be used in Pose Mode and Armature Edit Mode.'): '只能在姿态模式或骨架编辑模式使用本功能。',
        ('*', 'The actived object should be a valid armature object.'): '需要激活对象是一个有效的骨架对象。',
        ('*', 'Please select at least one bone.'): '请选中至少一根骨骼。',
        ('*', 'This function can only be used for armature of MMD model.'): '只能用于MMD模型的骨架。',
        ('*', 'Success. But the target bone is found to be among the selected bones, which may have unexpected results.'): '操作完成。但发现目标骨骼在选中的骨骼中，这可能产生意外的结果。',

        # material_panel.py
        ('*', 'diffuse'): '漫反射色',
        ('*', 'specular'): '高光色',
        ('*', 'ambient'): '环境色',
        ('*', 'alpha'): '不透明度',
        ('*', 'shininess'): '高光系数',
        ('*', 'double side'): '双面',
        ('*', 'ground shadow'): '地面影',
        ('*', 'self shadow map'): '自阴影贴图',
        ('*', 'self shadow'): '自阴影',
        ('*', 'outline'): '边缘',
        ('*', 'outline color'): '边缘色',
        ('*', 'outline weight'): '边缘权重',
        ('*', 'base tex'): '漫反射贴图路径',
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
        ('Operator', 'Select Invert'): '反选',
        ('*', 'Batch alter material props.'): '批量修改材质属性',
        ('*', 'Outdated! Please refresh the material list.'): '已过期！请刷新材质列表',
        ('Operator', 'Batch update'): '批量修改',
        ('*', 'select_type'): '选择方法',
        ('*', 'SELECT_ALL'): '全选',
        ('*', 'DESELECT_ALL'): '全部弃选',
        ('*', 'SELECT_INVERT'): '反选',

        ('*', 'Material Panel L2'): '材质面板2',
        ('Operator', 'Remove all redundant mmd shader group'): '删除所有冗余的MMDShader组',
        ('Operator', 'Copy Material From Data To Object Dialog'): '复制材质从网格数据到网格对象对话框',
        ('*', 'Reverse copy'): '反向复制',
        ('*', 'Swap'): '交换',
        ('*', 'Reference'): '引用',
        ('*', 'Keep origin slot link'): '保留原始材质槽链接',
        ('Operator', 'User Remap Material From Data To Object Dialog'): '重映射材质引用从网格数据到网格对象对话框',
        ('Operator', 'Copy Material From Actived To Selected Object Dialog'): '从激活对象复制材质到选择对象对话框',
        ('*', 'Only active material slot'): '仅激活材质槽',
        ('Operator', 'Reload All Image'): '重载所有图像',
        ('Operator', 'Remove All Redundant Image'): '移除所有冗余图像',
        
        # material_func.py
        ('*', 'Please select at least one mesh object.'): '请选中至少一个网格对象。',
        ('*', 'No MMD materials were found in the selected mesh object.'): '在选择的网格对象中没有发现任何MMD材质。',
        ('*', 'The actived object should be a valid mesh object.'): '激活对象需要是一个有效的网格对象。',
        ('*', 'At least one other mesh object needs to be selected in addition to the active object.'): '除了激活对象还需要选中至少一个其他网格对象。',

        # morph_panel.py
        ('*', 'Morph Panel'): '变形面板',
        ('Operator', 'Replace Material Morph Related Mesh Dialog'): '材质变形相关网格替换对话框',
        ('*', 'old mesh name patten'): '待替换网格名，支持通配符',
        ('*', 'new mesh name'): '新网格名',

        # morph_func.py
        ('*', 'The actived object should be a valid mmd root object.'): '要求激活对象是一个有效的mmd_root对象。',

        # rigidbody_panel.py
        ('*', 'Rigidbody Panel'): '刚体面板',
        ('Operator', 'Select all non bone ref rigid'): '选择所有没有引用任何骨骼的刚体',
        ('Operator', 'Auto rename selected rigidbody'): '自动重命名选择的刚体',
        ('Operator', 'Select joint by selected rigidbody'): '基于已选择的刚体选择关联的约束点(J点)',
        ('Operator', 'Select bone by selected rigidbody'): '基于已选择的刚体选择关联的骨骼',
        ('*', 'Kinematics'): '骨骼跟踪',
        ('*', 'Rot physics'): '骨骼位置跟踪',
        ('*', 'Physics'): '物理',
        ('Operator', 'Select Rigidbody By Physics Type Dialog'): '通过物理类型选择刚体',

        # rigidbody_func.py
        ('*', 'This function can only be used in Object Mode.'): '只能在物体模式使用本功能。',
        ('*', 'Please select at least one MMD rigidbody.'): '请至少选中一个MMD刚体。',
        ('*', 'The MMD root object associated with the MMD rigidbody does not exist.'): 'MMD刚体关联的MMD根对象不存在。',
        ('*', 'The MMD armature object associated with the MMD rigidbody does not exist.'): 'MMD刚体关联的MMD骨架对象不存在。',
        ('*', 'The active MMD model does not have any rigid bodies.'): '目标MMD模型没有任何刚体。',
        
        # joint_panel.py
        ('*', 'Joint Panel'): '约束点（J点）面板',
        ('Operator', 'Select all invalid joint'): '选择所有无效约束点',
        ('Operator', 'Auto Rename selected joint'): '自动重命名已选择的约束点',
        ('Operator', 'Select rigidbody by selected joint'): '基于已选择的约束点选择刚体',
        
        # joint_func.py
        ('*', 'Please select at least one MMD joint.'): '请至少选中一个MMD约束点。',

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
        ('*', 'Clean threshold'): '清除阈值',
        ('*', 'Max clean cycle'): '最多重复清理次数',
        ('*', 'Clean redundant frame'): '清理冗余帧',
        ('*', 'Active action'): '激活为当前动作',
        ('*', 'Clean start point'): '清理起始端点',
        ('*', 'Clean end point'): '清理结束端点',
        ('Operator', 'Clean Action Dialog'): '清理动作对话框',

        # action_func.py
        ('*', 'No found any active action on actived armature.'): '目标骨架发现没有激活的动画对象。',
        
        # other_panel.py
        ('*', 'Other Panel'): '其他面板',
        ('Operator', 'Delete all vrm obj'): '删除所有VRM对象',
        ('Operator', 'Delete all invalid driver'): '删除所有无效驱动器',
        ('Operator', 'Delete all ghost object'): '删除所有幽灵对象',
        
        # other_func.py

        # override_library_panel.py
        ('*', 'OverrideLibrary Panel'): '库覆盖面板',
        ('Operator', 'Batch Create OverrideLibrary Dialog'): '批量创建库覆盖对话框',
        ('*', 'Make local'): '本地化',
        ('*', 'Recusive children'): '递归子集',
        ('*', 'Mesh'): '网格',
        ('*', 'Mesh data'): '网格数据',
        ('*', 'Material'): '材质',
        ('*', 'Armature'): '骨架',
        ('*', 'Armature data'): '骨架数据',
        ('*', 'Empty'): '空对象',
        ('*', 'Camera'): '相机',
        ('*', 'Camera data'): '相机数据',
        ('Operator', 'All make local'): '全部本地化',

        # override_library_func.py

    },

# ------------------------------------------------------------------------------------------------------------
    "ja_JP": {
        # common
        ('*', 'Info'): '情報',
        ('*', 'Warning'): '警告',
        ('*', 'Error'): 'エラー',
        ('*', 'Success.'): '成功。',

        # bone_panel.py
        ('*', 'Bone Panel'): 'ボーンパネル',
        ('Operator', 'Clear selected bone roll'): '選択した骨のロールをクリア',
        ('Operator', 'Symmetric selected bones X'): '対称選択ボーン X',
        ('Operator', 'Auto setting and hide tip bone'): '先端ボーンの自動設定と非表示',
        ('Operator', 'Hide all uncontrollable bone'): 'すべての制御できない骨を隠す',
        ('Operator', 'Hide all physics bone'): 'すべての物理学の骨を隠す',
        ('*', 'Pose mode'): '姿勢モード',
        ('Operator', 'Select rigidbody by selected bone'): '選択したボーンによって剛体を選択',
        ('Operator', 'Disconnect all physical bone'): 'すべての物理的な骨を切り離す',
        ('Operator', 'Cancel disconnect all physical bone'): 'すべての物理ボーンの切断をキャンセル',

        # bone_func.py
        ('*', 'This function can only be used in Armature Edit Mode.'): 'この機能はアーマチュア編集モードでのみ使用できます。',
        ('*', 'This function can only be used in Pose Mode.'): 'この機能はポーズモードでのみ使用できます。',
        ('*', 'This function can only be used in Pose Mode and Armature Edit Mode.'): 'この機能は、ポーズ モードとアーマチュア エディット モードでのみ使用できます。',
        ('*', 'The actived object should be a valid armature object.'): 'アクティブ化されたオブジェクトは、有効なアーマチュア オブジェクトである必要があります。',
        ('*', 'Please select at least one bone.'): '少なくとも 1 つのボーンを選択してください。',
        ('*', 'This function can only be used for armature of MMD model.'): 'この機能はMMDモデルのアーマチュアにのみ使用できます。',
        ('*', 'Success. But the target bone is found to be among the selected bones, which may have unexpected results.'): '成功。 しかし、ターゲット ボーンが選択されたボーンの中にあることがわかり、予期しない結果になる可能性があります。',

        # material_panel.py
        ('*', 'diffuse'): '拡散色',
        ('*', 'specular'): 'ハイライトカラー',
        ('*', 'ambient'): 'アンビエントカラー',
        ('*', 'alpha'): '不透明度',
        ('*', 'shininess'): '鏡面反射係数',
        ('*', 'double side'): '両面',
        ('*', 'ground shadow'): '地影',
        ('*', 'self shadow map'): 'セルフ シャドウ マップ',
        ('*', 'self shadow'): 'セルフシャドウ',
        ('*', 'outline'): 'エッジ',
        ('*', 'outline color'): 'エッジの色',
        ('*', 'outline weight'): 'エッジ比重',
        ('*', 'base tex'): '拡散光カラー マップ パス',
        ('*', 'sphere tex'): '球状マップ パス',
        ('*', 'sphere tex type'): '球状マップ タイプ',
        ('*', 'is shared toon tex'): '共有トゥーン テクスチャを使用するかどうか',
        ('*', 'shared toon tex id'): 'トゥーン テクスチャ番号を共有する',
        ('*', 'toon tex'): 'トゥーン マップ パス',

        ('*', 'delimiter str'): 'デリミタ',
        ('*', 'alert_name_j'): '和名を変更するかどうか',
        ('*', 'del prefix'): '接頭辞を削除するか',
        ('*', 'del suffix'): '接尾辞を削除するかどうか',
        ('*', 'new prefix'): '接頭辞を追加する',
        ('*', 'new suffix'): '接尾辞を追加する',

        ('*', 'replace str'): '材料名の置換',
        ('*', 'old str'): '置き換えられたテキスト',
        ('*', 'new str'): '置き換えテキスト',

        ('*', 'backface culling'): '背面カリング',
        ('*', 'blend method'): '混合モード',
        ('*', 'shadow method'): '影モード',
        ('*', 'alpha threshold'): 'クランプ閾値',
        ('*', 'screen refraction'): 'スクリーン空間屈折',
        ('*', 'refraction depth'): '屈折深度',
        ('*', 'sss translucency'): 'SSS表面半透明',
        ('*', 'pass index'): 'チャンネル番号',

        ('*', 'Complete all operations with one click'): 'ワンクリックですべての変更操作を完了',

        ('*', 'Material Panel'): '材料パネル',
        ('Operator', 'Select Invert'): '選択を反転',
        ('*', 'Batch alter material props.'): '材料特性のバッチ変更',
        ('*', 'Outdated! Please refresh the material list.'): '時代遅れ材料リストを更新してください。',
        ('Operator', 'Batch update'): '一括編集',
        ('*', 'select_type'): '選び方',
        ('*', 'SELECT_ALL'): '全員が選ぶ',
        ('*', 'DESELECT_ALL'): 'すべて選挙を放棄する',
        ('*', 'SELECT_INVERT'): '逆選択',

        ('*', 'Material Panel L2'): '材料パネル2',
        ('Operator', 'Remove all redundant mmd shader group'): '冗長な MMDShader グループをすべて削除する',
        ('Operator', 'Copy Material From Data To Object Dialog'): 'メッシュ データからメッシュ オブジェクト ダイアログにマテリアルをコピー',
        ('*', 'Reverse copy'): '逆コピー',
        ('*', 'Swap'): '交換',
        ('*', 'Reference'): '引用',
        ('*', 'Keep origin slot link'): '元のマテリアル スロット リンクを保持',
        ('Operator', 'User Remap Material From Data To Object Dialog'): 'メッシュ データからメッシュ オブジェクト ダイアログへのマテリアル参照の再マップ',
        ('Operator', 'Copy Material From Actived To Selected Object Dialog'): 'アクティブオブジェクトからオブジェクトを選択するダイアログへマテリアルをコピーする',
        ('*', 'Only active material slot'): 'アクティブな材質の溝だけを使う',
        ('Operator', 'Reload All Image'): 'すべての画像を再ロード',
        ('Operator', 'Remove All Redundant Image'): '冗長画像をすべて除去',
        
        # material_func.py
        ('*', 'Please select at least one mesh object.'): '少なくとも 1 つのメッシュ オブジェクトを選択してください。',
        ('*', 'No MMD materials were found in the selected mesh object.'): '選択したメッシュ オブジェクトに MMD 素材が見つかりませんでした。',
        ('*', 'The actived object should be a valid mesh object.'): 'アクティブオブジェクトは有効なメッシュオブジェクトである必要がある。',
        ('*', 'At least one other mesh object needs to be selected in addition to the active object.'): 'アクティブオブジェクトに加えて、少なくとも1つの他のメッシュオブジェクトを選択する必要がある。',

        # morph_panel.py
        ('*', 'Morph Panel'): '変形パネル',
        ('Operator', 'Replace Material Morph Related Mesh Dialog'): '材料変形関連のメッシュ置換ダイアログ',
        ('*', 'old mesh name patten'): '置換するグリッドの名前。ワイルドカードがサポートされています',
        ('*', 'new mesh name'): '新しいグリッド名',

        # morph_func.py
        ('*', 'The actived object should be a valid mmd root object.'): 'アクティブ化オブジェクトは、有効な mmd_root オブジェクトである必要があります。',

        # rigidbody_panel.py
        ('*', 'Rigidbody Panel'): '剛体パネル',
        ('Operator', 'Select all non bone ref rigid'): 'どのボーンも参照していないすべての剛体を選択します',
        ('Operator', 'Auto rename selected rigidbody'): '選択した剛体の名前を自動的に変更',
        ('Operator', 'Select joint by selected rigidbody'): '選択した剛体に基づいて、関連する拘束点 (J ポイント) を選択します',
        ('Operator', 'Select bone by selected rigidbody'): '選択した剛体に基づいて関連付けられたボーンを選択します',
        ('*', 'Kinematics'): '骨追跡',
        ('*', 'Rot physics'): '骨の位置追跡',
        ('*', 'Physics'): '物理',
        ('Operator', 'Select Rigidbody By Physics Type Dialog'): '物理タイプによる剛体の選択',

        # rigidbody_func.py
        ('*', 'This function can only be used in Object Mode.'): 'この機能はオブジェクトモードでのみ使用できます。',
        ('*', 'Please select at least one MMD rigidbody.'): '少なくとも 1 つの MMD 剛体を選択してください。',
        ('*', 'The MMD root object associated with the MMD rigidbody does not exist.'): 'MMD リジッド ボディに関連付けられている MMD ルート オブジェクトが存在しません。',
        ('*', 'The MMD armature object associated with the MMD rigidbody does not exist.'): 'MMD 剛体に関連付けられた MMD Skeleton オブジェクトが存在しません。',
        ('*', 'The active MMD model does not have any rigid bodies.'): 'ターゲット MMD モデルには剛体がありません。',
        
        # joint_panel.py
        ('*', 'Joint Panel'): '拘束点（J 点）パネル',
        ('Operator', 'Select all invalid joint'): '無効な拘束点をすべて選択',
        ('Operator', 'Auto Rename selected joint'): '選択した拘束点の名前を自動的に変更',
        ('Operator', 'Select rigidbody by selected joint'): '選択した拘束点に基づいて剛体を選択する',
        
        # joint_func.py
        ('*', 'Please select at least one MMD joint.'): '少なくとも 1 つの MMD 拘束ポイントを選択してください。',
        
        # action_panel.py
        ('*', 'Action Panel'): 'アクションパネル',
        ('Operator', 'Fast Bake Action Dialog'): 'クイックベイクダイアログ',
        ('*', 'Action name'): 'アクション名',
        ('*', 'Frame start'): '開始フレーム',
        ('*', 'Frame end'): '終了フレーム',
        ('*', 'Frame step'): 'フレームステップ',
        ('*', 'No scale'): 'ズームを使わない',
        ('*', 'Override existing action'): '既存のアクションを上書きする',
        ('*', 'Disable constraints after baking'): 'ベイク後に制約を無効にする',
        ('*', 'Clean threshold'): 'クリーンアップのしきい値',
        ('*', 'Max clean cycle'): '最大繰り返しクリーンアップ回数',
        ('*', 'Clean redundant frame'): '冗長フレームのクリーンアップ',
        ('*', 'Active action'): '現在のアクションとしてアクティブ化',
        ('*', 'Clean start point'): '開始端点のクリーンアップ',
        ('*', 'Clean end point'): '終了端点のクリーンアップ',
        ('Operator', 'Clean Action Dialog'): 'クリーンアップアクションダイアログ',

        # action_func.py
        ('*', 'No found any active action on actived armature.'): 'ターゲット スケルトンは、アクティブなアニメーション オブジェクトを検出しませんでした。',

        # other_panel.py
        ('*', 'Other Panel'): 'その他のパネル',
        ('Operator', 'Delete all vrm obj'): 'すべての VRM オブジェクトを削除する',
        ('Operator', 'Delete all invalid driver'): '無効なドライブをすべて削除',
        ('Operator', 'Delete all ghost object'): '幽霊オブジェクトをすべて削除',
        
        # other_func.py

        # override_library_panel.py
        ('*', 'OverrideLibrary Panel'): 'ライブラリ オーバーレイ パネル',
        ('Operator', 'Batch Create OverrideLibrary Dialog'): '一括作成ライブラリ オーバーライド ダイアログ',
        ('*', 'Make local'): 'ローカリゼーション',
        ('*', 'Recusive children'): '再帰サブセット',
        ('*', 'Mesh'): 'グリッド',
        ('*', 'Mesh data'): 'グリッド データ',
        ('*', 'Material'): '材料',
        ('*', 'Armature'): 'スケルトン',
        ('*', 'Armature data'): 'スケルトンデータ',
        ('*', 'Empty'): '空のオブジェクト',
        ('*', 'Camera'): 'カメラ',
        ('*', 'Camera data'): 'カメラデータ',
        ('Operator', 'All make local'): 'すべてローカライズ',

        # override_library_func.py

    }

}
