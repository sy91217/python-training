# 集合的運算
s1={3,4,5}
print(3 in s1) # 用 in / not in 判斷資料有沒有在集合裡, 會回覆布林值(True/False)
print(3 not in s1)
s2={4,5,6,7}
s3=s1&s2 # 交集: 取兩個集合中相同的資料(&)
print(s3)
s3=s1|s2 # 聯集: 取兩個集合中的所有資料, 但不重覆選取
print(s3)
s3=s1-s2 # 差集: 從 s1 中, 減去和 s2 重疊的部分
print(s3)
s3=s1^s2 # 反交集: 取兩個集合中, 不重疊的部分
print(s3)
s=set("Hello") # set(字串), 將字串中的字母, 無排序且不重複的拆解成集合中的字元
# s={"l", "o", "H", "e"}
print(s) 
print("H" in s)
print("A" in s)
# 字典的運算: key-value pair 鍵值對
dic={"apple":"蘋果","bug":"蟲蟲"}
# dic["apple"]="小蘋果" # 更改字典中的 value
print(dic["apple"])
print("apple" in dic) # in / not in 判斷 key 是否存在(不能判斷 value)
print("apple" not in dic)
del dic["apple"] # del: 刪除字典中的鍵值對 (key-value pair)
print(dic)
dic={x:x*2 for x in [3,4,5]} # 從列表的資料產生字典
# dic={key:value for 代號 in [列表]
print(dic)
# 執行結果
# {3: 6, 4: 8, 5: 10}