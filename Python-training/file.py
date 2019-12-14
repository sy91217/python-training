# 檔案操作流程
# 開啟檔案 > 讀取或寫入 > 關閉檔案

# 基本語法
# 檔案物件=open(檔案路徑,mode=開啟模式)

# 開啟模式 (主要下列三種)
# 讀取模式 - r
# 寫入模式 - w
# 讀寫模式 - r+

# 讀取檔案
# 讀取全部文字
# 檔案物件.read()

# 一次讀取一行
# for 變數 in 檔案物件:
#     從檔案依序讀取每行文字到變數中

# 讀取 JSON 格式
# import json
# 讀取到的資料=json.load(檔案物件)

# 寫入檔案
# 寫入文字
# 檔案物件.write(字串)

# 寫入換行符號
# 檔案物件.write("這是範例文字\n") # \n = 換行

# 寫入 JSON 格式
# import json
# json.dump(要寫入的資料,檔案物件)

# 關閉檔案
# 基本語法
# 檔案物件.close()

# ***最佳實務***
# with open(檔案路徑, mode=開啟模式) as 檔案物件:
#     讀取或寫入檔案的程式
# 以上區塊會自動、安全的關閉檔案

# 儲存檔案
# file=open("data.txt", mode="w", encoding="utf-8") # 開啟 # 要寫中文記得指定使用 utf-8 編碼
# file.write("測試中文\n好棒棒") # 操作
# file.close() # 關閉

# 最佳實務範例
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("測試中文\n好棒棒")

# 讀取檔案
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     data=file.read()
# print(data)

# 最佳實務範例
# with open("int.txt", mode="w", encoding="utf-8") as file:
#     file.write("5\n3")

# 讀取檔案
# 把檔案中的數字資料, 一行一行的讀取出來, 並計算總合
# sum=0
# with open("int.txt", mode="r", encoding="utf-8") as file:
#     for line in file: # 一行一行的讀取
#         sum+=int(line)
# print(sum)

# 使用 JSON 格式讀取、複寫檔案
import json
# 從檔案中讀取 JSON 資料, 放入變數 data 裡面
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) # data 是一個字典資料
data["name"]="New Name" # 修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)

print("name: ", data["name"])
print("version: ", data["version"])