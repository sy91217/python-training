# 函式 (程式區塊): 程式碼包裝在一個區塊中, 方便隨時呼叫使用
# 定義 > 呼叫: 要先定義 (建立) 函式, 然後才能呼叫 (使用) 函式
# 基本語法
# def 函式名稱(參數名稱):
#     函式內部的程式碼

# 程式範例
# 定義一個印出 Hello 的函式
# def sayHello():
#     print("Hello")
# 定義可以印出任何訊息的函式
# def say(msg):
#     print(msg)

# 程式範例
# 定義一個可以做加法的函式
# def add(n1,n2):
#     result=n1+n2
#     print(result)

# 呼叫函式
# 基本語法: 函式名稱(參數資料)

# 程式範例
# def sayHello():
#     print("Hello")
# 呼叫上方定義的函式
# sayHello()

# 程式範例
# 定義可以印出任何訊息的函式
# def say(msg):
#     print(msg)
# 呼叫上方定義的函式
# say("Hello Function")
# say("Hello Python")

# 程式範例
# 定義一個可以做加法的函式
# def add(n1,n2): # 多個參數用逗號(,)隔開
#     result=n1+n2
#     print(result)
# 呼叫上方定義的函式
# add(3,4)
# add(7,8)

# 回傳值

# 基本語法
# def 函式名稱(參數名稱):
#     函式內部的程式碼
#     return # 結束函式, 回傳 None

# 基本語法
# def 函式名稱(參數名稱):
#     函式內部的程式碼
#     return 資料 # 結束函式, 回傳「資料」

# 程式範例
# 函式回傳 None
# def say(msg):
#     print(msg)
#     return
# 呼叫函式, 取得回傳值
# value=say("Hello Function")
# print(value) # 印出 Hello

# 程式範例
# 函式回傳字串 Hello
# def add(n1,n2):
#     result=n1+n2
#     return "Hello" # 雖然計算出 7, 但是回傳"Hello", 無意義
# 呼叫函式, 取得回傳值
# value=add(3,4)
# print(value) # 印出 Hello

# 程式範例
# 函式回傳 n1+n2 的結果
# def add(n1,n2):
#     result=n1+n2
#     return result
# 呼叫函式, 取得回傳值
# value=add(3,4)
# print(value) # 印出 7


# 定義函式
# 函式內部的程式碼, 若是沒有做函式呼叫, 就不會執行
# def multiply():
#     print(3*4)
# 呼叫函式
# multiply()

# 定義函式
# def multiply(n1,n2):
#     print(n1*n2)
# 呼叫函式
# multiply(3,4) # 可自行填寫數字, 有彈性
# multiply(10,8)

# 定義函式
# def multiply(n1,n2):
#     print(n1*n2)
#     return # 回傳值 None, 跟沒寫 return 一樣
# 呼叫函式
# value=multiply(3,4)
# print(value)
# 執行結果
# 12 # value 執行乘法, 因 print(n1,n2) 而印出 12
# None # 由於 return, 因此回傳值為 None, value=None, print(value), 印出 None

# 定義函式
# def multiply(n1,n2):
#     print(n1*n2)
#     return n1*n2
# 呼叫函式
# value=multiply(3,4)
# print(value)
# 執行結果
# 12
# 12 # 結果相同

# 定義函式
# def multiply(n1,n2):
#     print(n1*n2)
#     return n1*n2
# 呼叫函式
# value=multiply(3,4)
# print(value)
# 執行結果
# 12
# 12 # 結果相同

# 定義函式
# def multiply(n1,n2):
#     return n1*n2
# 呼叫函式
# value=multiply(3,4)+multiply(10,5) # (3*4)+(10*5)
# print(value)
# 執行結果
# 62 # (3*4)+(10*5)=62

# 函式可用來做程式的包裝: 同樣的邏輯可以重複利用
# 老師寫的
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)
# # 呼叫函式
calculate(10)
calculate(20)

# 自己先想的
# 定義函式
def calculate(n1,n2):
    sum=0
    for n in range(n1,n2):
        sum=sum+n
    print(sum)
# 呼叫函式
calculate(1,11)
calculate(1,21)  

# 上述函式將下列語法用函式來做程式的包裝
# sum=0
# for n in range(1,11):
#     sum=sum+n
# print(sum)

# sum=0
# for n in range(1,21):
#     sum=sum+n
# print(sum)