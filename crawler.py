## 抓取 PPT 電影版的網頁原始碼
import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個request物件，附加 Request Headers 的資訊 (user-agent:) 為了讓你看起來像一個正常的使用者
request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  # 把網站資料讀取下來放入變數 data

# print(data)

## 解析原始碼，取得文章標題
import bs4  # pip install beautifulsoup4

root = bs4.BeautifulSoup(data, "html.parser")  # HTML格式去做解析
# print(root.title.string)  # 加入 .string 表示取得文字就好 ( 取得網頁標題 )
# titles = root.find("div", class_="title")  # .find尋找 class  = "title" 的 div 標籤
titles = root.find_all("div", class_="title")  # .find_all 尋找所有 class  = "title" 的 div 標籤 (list type 形式)
for title in titles:
    if title.a != None:  # 如果標題含有 a 標籤表示文章沒有被刪除，那就印出來
        print(title.a.string)

# print(titles.a.string)  # title 代表 div 、 .a 代表 a 標籤 、 .string 表示取得a標籤裡的文字就好