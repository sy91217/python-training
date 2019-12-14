# 類別的定義與使用
# 類別: 可封裝變數或函式(封裝的變數或函式, 統稱為類別的屬性)
# 定義 > 使用
# 要先定義(建立)類別, 然後才能使用類別中封裝的屬性

# 定義類別
# 基本語法
# class 類別名稱: # 類別名稱通常習慣首字大寫
#     定義封裝的變數
#     定義封裝的函式

# 程式範例
# 定義 Test 類別
# class Test:
#     x=3 # 定義變數
#     def say(): # 定義函式
#         print("Hello")

# 使用類別
# 基本語法
# 類別名稱.屬性名稱

# 程式範例
# 定義 Test 類別
# class Test:
#     x=3
#     def say():
#        print("Hello")
# 使用 Test 類別
# Test.x+3 # 取得屬性 x 的資料 3, 再 + 3 
# Test.say() # 呼叫屬性 say 函式

# 定義類別、與類別屬性 (封裝在類別中的變數和函式)
# 定義一個類別 IO, 有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs=["console","file"] # 支援的資料來源
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from", src)

# 使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")