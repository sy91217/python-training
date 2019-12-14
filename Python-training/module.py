# 模組的載入與使用
# 模組(獨立的城市檔案): 將程式寫在一個檔案中, 此檔案可重複載入使用
# 載入 > 使用: 先在入模組, 再使用模組中的函式或變數
# 基本語法
# import 模組名稱
# 或
# import 模組名稱 as 模組別名 # 幫模組另外取名, 可能因模組名稱太長, 取較短的別名以方便使用

# 使用模組
# 基本語法
# 模組名稱或別名.函式名稱(參數資料)
#     模組名稱或別名.變數名稱

# 內建模組
# sys 模組: 取得系統相關資訊
# 程式範例
# 載入 sys 模組
# import sys
# 使用 sys 模組
# print(sys.platform) # 印出作業系統
# print(sys.maxsize) # 印出整數型態的最大值
# print(sys.path) # 印出搜尋模組的路徑
# 或
# 載入 sys 模組
# import sys as sys
# 使用 sys 模組
# print(s.platform) # 印出作業系統
# print(s.maxsize) # 印出整數型態的最大值
# print(s.path) # 印出搜尋模組的路徑

# 自訂模組
# 建立幾何運算模組
# 建立檔案 geometry.py, 定義平面幾何運算用的函式
# 載入與使用
# 載入 geometry 模組, 並使用模組中定義的功能

# 載入內建的 sys 模組並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)
# 執行結果
# win32
# 2147483647

# 建立 geometry 模組, 載入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# result=geometry.slope(1,2,5,6)
# print(result)
# 執行結果
# 5.656854249492381
# 1.0

# 調整搜尋模組的路徑
import sys
sys.path.append("modules") # 在模組裡的搜尋路徑列表中【新增路徑】
print(sys.path) # 印出模組的搜尋路徑
# 執行結果
# ['C:\\Users\\user\\Desktop\\Python-training', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages', 'modules']
# 模組要放在這些路徑中, 才找的到
import geometry
print(geometry.distance(1,1,5,5))
# 執行結果出現 Error, 因為移動模組位置, 新增路徑後就可正常執行