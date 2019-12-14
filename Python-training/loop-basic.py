# while 迴圈
# 基本語法
# while 布林值:
#     若布林值為 True, 執行命令
#     回到上方, 做下一次的迴圈判斷
# 程式範例
# n=1
# while n<5:
#     print("變數 n 的資料是:", n)
#     n+=1
# 執行結果
# 變數 n 的資料是: 1
# 變數 n 的資料是: 2
# 變數 n 的資料是: 3
# 變數 n 的資料是: 4
# 由於 n>=5, 因此迴圈終止

# for 迴圈
# 基本語法
# for 變數名稱 in 列表或字串:
#     將列表中的項目或字串中的字元逐一取出, 逐一處理
# 程式範例
# for x in [4,1,2]:
#     print("逐一取得列表中的資料", x)
# 執行結果
# 逐一取得列表中的資料 4
# 逐一取得列表中的資料 1
# 逐一取得列表中的資料 2
# for c in "Hello":
#     print("逐一取得字串中的字元:", c)
# 執行結果
# 逐一取得字串中的字元 H
# 逐一取得字串中的字元 e
# 逐一取得字串中的字元 l
# 逐一取得字串中的字元 l
# 逐一取得字串中的字元 o

# for 迴圈經常搭配 range(), 可製造出連續數字的列表
# for 變數名稱 in range(3):
# 相當於
# for 變數名稱 in range[0,1,2]:

# for 變數名稱 in range(3,6): # 包含開頭, 不包含結尾的編號
# 相當於
# for 變數名稱 in [3,4,5]:

# while 迴圈
# 無窮迴圈
# n=1
# while True:
#     print(n)
#     n+=1
# ctrl+c 強制結束
# 1+2+3+...+10
# n=1
# sum=0 # 紀錄累加的結果
# while n<=10: # 有縮排: 迴圈內部, 沒縮排: 迴圈外部
#     sum=sum+n
#     n+=1
#　print(sum)

# for 迴圈
# for x in [3,5,1]:
#     print(x)
# for x in "Hello":
#     print(x)
# for x in range(5):
#     print(x)
# for x in range(5,10):
#     print(x)
# 1+2+3+...+10
sum=0
for x in range(1,11):
    sum=sum+x
print(sum)