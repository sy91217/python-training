# 網路連線、公開資料串接
# 載入模組
# import urllib.request

# 下載特定網址資料
# import urllib.request as request
# with request.urlopen(網址) as response: # 連線網址後, python 連線後給我們 response 物件
#     data=response.read()
# print(data)

# 公開資料
# 適合的資料來源
# 台北市政府公開資料 (https://data.taipei/#/)
# 確認資料格式 : JSON、CSV、或其他格式
# 解讀 JSON 格式 (使用內建的 json 模組)

# 網路連線
# import urllib.request as request
# src="http://www.ntu.edu.tw/" # 臺大網址
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") # 取得台灣大學網站的原始碼 (HTML、CSS、JS)
# print(data)

# 串接、擷取公開資料
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=24c9f8fe-88db-4a6e-895c-498fbc94df94"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理 json 資料格式
# print(data) # 檢驗網頁的結果

# 將學校名稱列表出來
clist=data["result"]["results"]
with open("open-data.txt", "w", encoding="utf-8") as file:
    for agency in clist:
        file.write("機構名稱: "+agency["o_tlc_agency_name"]+"\n") # 抓出資料並換行
# print(agency["o_tlc_agency_name"]) # 檢驗選取的結果是否有誤 # o_tlc_agency_name 是資料中的 key, 印出對應的 value
