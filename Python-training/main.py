# 封包(包含模組的資料夾): 用來整理、分類模組程式
# 建立封包:
# 專案檔案配置
# - 專案資料夾
#     - 主程式.py
#     - 封包資料夾
#         - __init__.py # 一定要有
#         - 模組一.py
#         - 模組二.py

# 專案檔案配置範例
# - 專案檔案夾
#     - main.py
#     - geometry
#         - __init__.py
#         - point.py
#         - line.py

# 基本語法
# import 封包名稱.模組名稱

# 主程式
import geometry.point as point
result=point.distance(3,4)
print("距離", result)

import geometry.line as line
result=line.slope(1,1,3,3)
print("斜率", result)