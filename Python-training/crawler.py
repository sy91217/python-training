# 網路爬蟲 Web Crawler 基本篇
# 基本流程
# 1. 連線到特定網址, 抓取資料
# 2. 解析資料, 取得實際想要的部分

# 抓取資料: 盡可能地, 讓程式模仿一個普通使用者的樣子

# 解析資料
# JSON 格式資料: 使用內建的 json 模組即可

# HTML 格式資料: 使用第三方套件 BeautifulSoup 來做解析
# <html>
#     <head>
#         <title>HTML 格式</title>
#     </head>
#     <body>
#         <div class="list">
#             <span>階層結構</span>
#             <span>樹狀結構</span>
#         </div>
#     </body>
# </html>

# PIP 套件管理工具 (安裝 Python 時, 就一起安裝在電腦中了)
# 安裝 BeautifulSoup: pip install beautifulsoup4

# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件. 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}) # User-Agent: 使用甚麼瀏覽器及作業系統
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

# 解析原始碼, 取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser") # 資料丟給 BeautifulSoup, 協助我們解析 HTML 格式文件
# print(root.title.string) # root 代表整份網頁, title 代表網頁標籤, string 代表標籤中的字串
titles=root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤, find_all 找出所有的
# print(titles) # 印出 網頁標籤 title 中, a 後面的字串
for title in titles:
    if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除), 則印出來
        print(title.a.string)

# Steps
# 到 https://www.ptt.cc/bbs/movie/index.html 中, 右鍵點擊 "檢視網頁原始碼" (Ctrl + U), 是網頁背後真正的資料
# 大部分網站不喜歡不像正常使用者的連線, 會無法抓取資料, 因此要使連線像一個正常的使用者
# 到 https://www.ptt.cc/bbs/movie/index.html 中, 按 F12 (開發人員工具)
# 點選上方選單 "Network", 按 F5 (重新整理), 選取 "All", 點 "index.html"
# 點 "Headers", 會顯示連線到該網址的細節, 用瀏覽器連線到 PTT 伺服器所附加的資訊, 代表一般使用者使用時發送的資訊, coding 時也要一樣
# 最下方的 "User-Agent" 很重要, 去掉空白, 要一模一樣