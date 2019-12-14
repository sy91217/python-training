# Pandas 資料分析 - 基礎篇
# Pandas: 概念類似試算表的資料分析套件
# 基礎學習項目
# 1. 安裝 Pandas 套件
# 2. 認識單維度的資料 Series
# 3. 認識雙維度的資料 DataFrame

# 準備環境
# PIP 套件管理工具
# 安裝 Pandas: pip install pandas

# Series: 單維度的資料, 像是列表、或是試算表中直向的欄位資料
# 建立 Series
# 載入 Pandas 模組
# import pandas as pd
# 以列表資料為底, 建立 Series
# pd.Series(資料列表)

# 使用 Series
# import pandas as pd
# data=pd.Series(資料列表)
# data.max() # 找出最大值
# data.median() # 計算中位數
# data=data*2 # 放大兩倍

# DataFrame: 雙維度的資料, 像是一個表格, 有欄和烈的概念
# 建立 DataFrame
# 載入 Pandas 模組
# import pandas as pd
# 以字典資料為底, 建立 DataFrame
# pd.DataFrame(字典)

# 取得特定欄 (直向)
# import pandas as pd
# data=pd.DataFrame(字典)
# data["欄位名稱"]

# 取得特定列 (橫向)
# import pandas as pd
# data=pd.DataFrame(字典)
# data.iloc[列編號] # 列編號按順序由 0 開始累加

# 檔名不能用 pandas, 會跟內建模組衝突

# 載入 pandas 模組
import pandas as pd
# 建立 Series
# data=pd.Series([20,10,15])
# 基本 Series 操作
# print(data)
# print("Max", data.max())
# print("Median", data.median())
# print(data*2)
# data=data==20 # data 有沒有跟 20 相等, 每個去做比較, 得到布林值
# print(data)

# 建立 DataFrame
data=pd.DataFrame({
    "name":["Jay","Hitachi","Allen"],
    "salary":["1000","2000","3000"]
})
# 基本 DataFrame 操作
# print(data)

# 取得特定的欄位
# print(data["name"])
# print(data["salary"])
# 取得特定的獵
print(data.iloc[0]) # iloc = ilocaion, 輸入列編號, 第一列 是 0
print(data.iloc[1]) # 印出第二列
