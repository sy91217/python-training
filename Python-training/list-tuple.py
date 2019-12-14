# 有序可變動列表 List: 中括號[]
grades=[12,60,15,70,90]
# grades=[12,60,15,70,90]
#          0  1  2  3  4
grades[0]=55 # 把 55 放到列表中的第一個位置
print(grades)
print(grades[3])
# grade[1:4]=[] # 連續刪除列表中從編號 1 到編號 4(不包括) 的資料
print(grades[1:4])
# grades=grades+[12,33] # 新增資料到列表中, 接續在最後一個編號後面
print(grades)
length=len(grades) # 取得列表的長度 len(列表資料)
print(length)

data=[[3,4,5],[6,7,8]] # 列表中又包含列表
print(data)
data[0][0:2]=[5,5,5] # 將列表中第一個列表內編號 0 到編號 2(不包含) 改成 [5,5,5]
print(data)
print(data[0][0:]) # 印出 data 列表中第一個列表的編號 0 到最後一個編號

# 有序不可變動列表 Tuple: 小括號()
data=(3,4,5)
# data[0]=5 # 錯誤: Tuple 的資料不可以變動
print(data)