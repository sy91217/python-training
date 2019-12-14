# 函式參數詳解
# 預設資料
# 基本語法
# def 函式名稱(參數名稱=預設資料):
#     函式內部的程式碼

# 程式範例
# 參數 msg 預設資料為 "Hello"
# def say(msg="Hello"):
#     print(msg)
# 印出 Hello Function
# say("Hello Function")
# say() # 因為沒有放參數資料, 所以印出預設資料 Hello

# 名稱對應
# 無限參數
# 基本語法
# def 函式名稱(*無限參數): # 參數前加星星(*), 代表無限長度的參數
#     無限參數以 Tuple 資料型態處理函式內部的程式碼
# 呼叫函式, 可傳入無限數量的參數
# 函式名稱(資料一, 資料二, 資料三) # 可放入不定數量的資料

# 程式範例
# 函式接受無限參數 msg
# def say(*msgs):
    # 以 Tuple 的方式處裡
    # for msg in msgs:
    #     print(msg)
# 呼叫函式, 傳入三個參數資料
# say("Hello","Arbitary","Arguments")
# 執行結果
# Hello
# Arbitary
# Arguments

# 參數的預設資料
# def power(base,exp=0): # base:基數, exponent(exp):次方(冪)值, exp預設為0
#     print(base**exp)
# power(3,2) # 3**2=9
# power(4) # 若 exp 無預設值, 則會顯示 Error, 但現在 exp 預設值為 0, 因此計算 4**0=1

# 使用參數名稱對應
# def divide(n1,n2=1):
#     print(n1/n2)
# divide(2,4) # 2/4=0.5
# divide(2) # 若 n2 無預設值, 則會顯示 Error, 但現在 n2 預設值為 1, 因此計算 2/1=2.0
# divide(n2=2,n1=4) # 指定參數名稱給資料, 則會按照名稱對應計算, 4/2=2.0

# 無限/不定 參數資料
def avg(*ns): # 前有*是不定長度的參數
    sum=0
    for n in ns: # Tuple 迴圈, 將數字一個一個抓出來
        sum=sum+n # 將每個數字加總
    print(sum/len(ns)) # 總和/列表長度
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)
# 執行結果
# 3.5
# 6.0
# -1.0