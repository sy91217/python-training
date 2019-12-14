# 亂數(random)、統計(statistics)模組(python 內建模組)
# 亂數模組
# 載入模組
# import random

# 隨機選取
# import random
# 從列表中隨機選起 1 個資料
# random.choice([0,1,5,8])
# 從列表中隨機選取 2 個資料
# random.sample([0,1,5,8],2)

# 隨機調換順序
# import random
# 將列表的資料「就地」隨機調換順序
# data=[0,1,5,8]
# random.shuffle(data)
# print(data)

# 隨機亂數
# import random
# 取得 0.0 ~ 1.0 之間的隨機亂數 (每個出現機率相同)
# random.random()
# random.uniform(0.0,1.0) # uniform: 出現機率相同

# 常態分配亂數
# import random
# 取得平均數 100、標準差 10 的
# 常態分配亂數
# random.normalvariate(100,10) # 0(平均數,標準差)

# 統計模組
# 載入模組
# import statistics

# 計算平均數
# import statistics
# 計算列表中數字的平均數
# statistics.mean([1,4,6,9])

# 計算中位數
# import statistics
# 計算列表中數字的中位數
# statistics.median([1,4,6,9])

# 計算標準差
# import statistics
# 計算列表中數字的標準差
# statistics.stdev([1,4,6,9])

# 隨機模組
# import random
# 隨機選取
# data=random.choice([1,5,6,10,20])
# print(data)
# data=random.sample([1,5,6,10,20],3)
# print(data)

# 隨機調換順序 # shuffle: 洗牌(隨機調換順序)
# data=[1,5,8,20]
# random.shuffle(data) # 對 data 本身進行資料調換
# print(data)

# 隨機取得亂數
# data=random.random() # 0.0 ~ 1.0 之間的隨機亂數
# 相當於
# data=random.uniform(0.0,1.0)
# print(data)
# data=random.uniform(60,100) # 60 ~ 100 之間的隨機亂數
# print(data)

# 取得常態分配亂數
# 平均數 100, 標準差 10, 得到的資料多數在 90 ~ 100 之間
# data=random.normalvariate(100,10)
# print(data)

# 平均數 0, 標準差 5, 得到的資料多數在 -5 ~ 5 之間
# data=random.normalvariate(0,5)
# print(data)

# 統計模組
import statistics as stat # 將 stat 當作別名
# 平均數
data=stat.mean([1,4,5,8])
print(data)
# 中位數 (不易受離群值影響)
data=stat.median([1,2,3,4,5,8,100])
print(data)
# 標準差 (可測量一組數值的離散程度)
data=stat.stdev([1,2,3,4,5,8,10])
print(data)