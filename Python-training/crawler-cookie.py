# 網路爬蟲 Web Crawler - Cookie
# 基本流程
# 1. 連線到特定網址, 抓取資料
# 2. 解析資料, 取得實際想要的部分
# 抓取資料: 盡可能地, 讓程式模仿一個普通使用者的樣子

# Cookie: 網站存放在瀏覽器的一小段內容
# 與伺服器的互動: 連線時, 放在 Request Headers 中送出

# 追蹤連結
# HTML 超連結
# <html>
#     <head>
#         <title>HTML 格式</title>
#     </head>
#     <body>
#         <a href="https://www.google.com/">Google</a>
#     </body>
# </html>

# 連續抓取頁面實務: 解析頁面的超連結, 並結合程式邏輯完成

# 抓取 PTT 八卦板的網頁原始碼 (HTML)
# 進入八卦板前, 會出現 "是否18歲的確認畫面"

import urllib.request as req
def getData(url): # 包裝抓取單一頁面的程式碼: 將原本下面的 code 全部縮排, 放入函式中

    # 建立一個 Request 物件. 附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
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
    # 抓取上一頁的連結
    nextLink=root.find("a", string="‹ 上頁") # 找到內文是 "< 上頁" 的 a 標籤
    return nextLink["href"]
    # print("https://www.ptt.cc"+nextLink["href"]) # 印出標籤中的 href 屬性

# 主程序: 抓取一個頁面的標籤
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5: # 看使用者要抓幾頁
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
    # print(pageURL)

# Steps
# 搜尋 "PTT 八卦板", 在搜尋頁面按 F12 > Application > Cookies > https://www.ptt.cc, 可看到有存放資料
# 按上方 Clear All, 可刪除 Cookie, 再重新整理一次, 又會跳出 over18 之訊息, 只要確認過一個即可
# cookie 會放在 index.html > Headers > Request Headers, 重點是 over18=1
# 到 https://www.ptt.cc/bbs/movie/index.html 中, 右鍵點擊 "檢視網頁原始碼" (Ctrl + U), 是網頁背後真正的資料
# 大部分網站不喜歡不像正常使用者的連線, 會無法抓取資料, 因此要使連線像一個正常的使用者
# 到 https://www.ptt.cc/bbs/movie/index.html 中, 按 F12 (開發人員工具)
# 點選上方選單 "Network", 按 F5 (重新整理), 選取 "All", 點 "index.html"
# 點 "Headers", 會顯示連線到該網址的細節, 用瀏覽器連線到 PTT 伺服器所附加的資訊, 代表一般使用者使用時發送的資訊, coding 時也要一樣
# 最下方的 "User-Agent" 很重要, 去掉空白, 要一模一樣
# 讓程式動態追蹤上一頁的超連結, 抓取每個頁面, 對 "上頁" 按右鍵 點 "檢查", 可發現在網頁中是 a 的標籤, 點選兩下即可複製
# 利用過去學到的函式及技巧控制要爬幾頁