# Pandas 資料分析 - Series
# Series: 單維度的資料, 像是列表、或是試算表中直向的欄位資料
# 建立 Series
# 載入 Pandas 模組
# import pandas as pd
# 以列表資料為底, 建立 Series
# pd.Series(資料列表)

# 資料索引: 資料的獨立編號 (像是試算表中最左邊的編號)
# 內建索引
# 載入 Pandas 模組
# import pandas as pd
# 以列表資料為底, 建立 Series
# pd.Series(資料列表)

# 自訂索引
# 載入 Pandas 模組
# import pandas as pd
# 以列表資料為底, 建立 Series
# pd.Series(資料列表,index=索引列表)

# 觀察資料
# 資料型態
# import pandas as pd
# data=pd.Series(資料列表)
# 印出 size 屬性
# print(data.index)

# 取得資料
# 根據順序取值
# import pandas as pd
# data=pd.Series(資料列表)
# 取得資料 data[順序]
# print(data[1]) # 由 0 開始, 1 代表取得第 2 個資料

# 根據索引取值
# import pandas as pd
# data=pd.Series(資料列表, index=索引列表)
# 取得資料 data[索引]
# print(data[索引])

# 數字運算: 數學、統計相關
# import pandas as pd
# data=pd.Series([3,10,20,5,-12])
# 各種數學、統計運算
# print(data.sum(), data.max(), data.prod()) # prod() 乘法總和
# print(data.mwan(), data.median(), data.std())
# print(data.nlargest(3), data.nsmallest(2)) # nlargest() 前 n 大的數字, nsmallest 最小的 n 個數字

# 字串運算
# 字串操作相關
# import pandas as pd
# data=pd.Series(["您好","Python","Pandas"])
# 各種字串操作, 都定義在 str 底下
# print(data.str.lower(), data.str.upper(), data.str.len()) # lower() 把所有字串變小寫, upper() 把所有字串變大寫, len() 取得每個字串的長度
# print(data.str.cat(sep=","), data.str.contains("P")) # cat(sep=",") 把所有字串用逗號串在一起, 串成一個字串 (可把逗號改成其他符號), contains("P") 判斷字串中是否包含 P
# print(data.str.replace("您好","Hello")) # replace 將字串取代成其他字串

# 載入 pandas 模組
import pandas as pd
# 資料索引
data=pd.Series([5,4,-2,3,7.0], index=["a","b","c","d","e"]) # 資料有幾個, 索引就有幾個
# print(data)

# 觀察資料
# print("資料型態", data.dtype) # 像是 int, float 等等
# print("資料數量", data.size)
# print("資料索引", data.index) # 字串 = object

# 取得資料: 根據順序、根據索引
# print(data[2], data[0])
# print(data["e"], data["d"])

# 數字運算: 基本、統計、順序
# print("最大值", data.max())
# print("總和", data.sum())
# print("標準差", data.std())
# print("中位數", data.median())
# print("最大的三個數", data.nlargest(3)) # data.nsmallest(2) 最小的兩個數

# 字串運算: 基本、串接、搜尋、取代
data=pd.Series(["您好","Python","Pandas"])
print(data.str.lower()) # 全部變小寫, 中文不變
print(data.str.len()) # 算出每個字串的長度
print(data.str.cat(sep=", ")) # 把字串串起來, 可以自訂串接的符號
print(data.str.contains("P")) # 判斷每個字串是否包含特定的字元, 得出的結果是布林值
print(data.str.replace("您好","Hello")) # 將某個字串取代成其他字串
