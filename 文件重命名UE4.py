"""
说明：使用UE4 Python，批量重命名unreal assets

作者：钟小二宝
E-mail:1023462838@qq.com
时间：2021年3月4日
"""

import unreal
from unreal import EditorUtilityLibrary
"""
资产重命名-重置
"""


def rename_asset_reset(asset_type, asset_name, index, asset_variation):
    # instance of unreal classes
    editor_util = unreal.EditorUtilityLibrary()

    # 获取需要重命名的资产
    selected_assets = editor_util.get_selected_assets()

    for asset in selected_assets:
        assetname = ("{}_{}_{}_{}").format(asset_type, asset_name, index, asset_variation)
        index += 1
        # 资产重命名
        editor_util.rename_asset(asset, assetname)


def rename_assets():
    # 资产前缀
    asset_type = "Type"
    # 资产名称
    asset_name = "assetName"
    # 起始序列数
    index = 0
    # 资产后缀
    asset_variation = "VA"

    rename_asset_reset(asset_type, asset_name, index, asset_variation)


def main():
    rename_assets()


if __name__ == "__main__":
    main()
