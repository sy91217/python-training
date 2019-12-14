# break 強制結束迴圈
# while 布林值:
#     break
# 程式範例
# n=1
# while n<5:
#     if n==3:
#         break
#     n+=1
# print(n) # 印出 3

# for 變數名稱 in 列表/字串:
# break

# continue 強制繼續下一圈
# while 布林值:
#     continue
# for 變數名稱 in 列表/字串:
#     continue
# 程式範例
# n=0
# for x in [0,1,2,3]: # x 會跑 4 圈, 分別為 0, 1, 2, 3
#     if x%2==0: # 若餘數=0, 強制下一圈
#         continue   # x=0, 因餘數為0, 所以強制下一圈, 執行 x=1,
#     n+=1           # x=1, 餘數不為0,   n+=1 => n=1, 執行 x=2,
# print(n) # 印出 2  # x=2, 因餘數為0, 所以強制下一圈, 執行 x=3,
#                    # x=3, 餘數不為0,   n+=1 => n=2, print(n) => 2

# else
# 基本語法
# while 布林值:
#     若布林值為 True, 執行命令
#     回到上方, 做下次的迴圈判定
# else:
#     迴圈結束前, 執行此區塊的命令 # while 跑完後執行
# 程式範例
# n=1
# while n<5:
#     print("變數 n 的資料是:", n)
#     n+=1
# else:
#     print(n) # 結束迴圈前, 印出 5
# 執行結果
# 變數 n 的資料是: 1
# 變數 n 的資料是: 2
# 變數 n 的資料是: 3
# 變數 n 的資料是: 4
# 5

# 基本語法
# for 變數名稱 in 列表/字串
#     將列表中的項目或字串中的字元逐一取出, 逐一處理
# else:
#     迴圈結束前, 執行此區塊的指令 # while 跑完後執行
# 程式範例
# for c in "Hello":
#     print("逐一取得字串中的字元", c)
# else:
#     print(c) # 結束迴圈前, 印出 o
# 執行結果
# 逐一取得字串中的字元 H
# 逐一取得字串中的字元 e
# 逐一取得字串中的字元 l
# 逐一取得字串中的字元 l
# 逐一取得字串中的字元 o
# o

# break 的簡易範例
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) # 印出迴圈中的 n
#     n+=1
# print("最後的 n: ", n) # 印出迴圈結束後的 n
# 執行結果
# 0
# 1
# 2
# 最後的 n:  3

# continue 的簡易範例
n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print("最後的 n: ", n)
# 執行結果
# 1
# 3
# 最後的 n:  2

# else 的簡易範例
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) # 印出 0+1+2+...+10 的結果 # 印出 55

# 綜合範例: 找出整數平方根
# 輸入 9, 得到 3
# 輸入 11, 得到【沒有】整數的平方根
# n=input("輸入一個正整數: ")
# n=int(n) # 轉換輸入成數字
# for i in range(n): # i 從 0 ~ n-1
#     if i*i==n:
#         print("整數平方根", i)
#         break # 用break 強制結束迴圈時, 不會執行 else 區塊
# else:
#     print("沒有整數平方根")

