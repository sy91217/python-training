# 基本語法一
# if 布林值:
#   若布林值為 True, 執行命令 (句首記得 Tab 縮排)
# 基本語法二
# if 布林值:
#   若布林值為 True, 執行命令
# else:
#   若布林值為 False, 執行命令
# 基本語法三
# if 布林值一:
#   若布林值一為 True, 執行命令
# elif 布林值二:
#   若布林值二為 True, 執行命令
# else:
#   若布林值一和二都 False, 執行命令
# 程式範例:
# x=input("請輸入數字:") # 基本輸入為字串型態
# x=int(x) # 轉換為整數型態/ float 為轉換成浮點數(小數)型態
# if x>200: # 布林值
#     print("大於 200")
# elif x>100:
#     print("大於100, 小於200")
# else:
#     print("小於 100")
# 目前不支援 switch 語法

# 判斷式
# if True: # 若改成 if False, 會印出 False 執行
#     print("True 執行")
# else:
#     print("False 執行")
# x=input("請輸入數字: ") # 取得字串形式的使用者輸入
# x=int(x) # 將字串型態轉換成數字型態
# x=int(input("請輸入數字: ")) # 上述兩式合併
# if x>200:
#     print("大於 200")
# elif x>100:
#     print("大於 100, 小於等於 200")
# else:
#     print("小於等於 100")

# 四則運算
n1=float(input("請輸入數字一: "))
n2=float(input("請輸入數字二: "))
op=input("請輸入運算: +, -, *, /")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")