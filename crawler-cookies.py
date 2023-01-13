## 抓取 PPT 八卦版的網頁原始碼
import urllib.request as req

def getURL(url):
    # 建立一個request物件，附加 Request Headers 的資訊 (user-agent:) 為了讓你看起來像一個正常的使用者
    request = req.Request(url, headers = {
        "cookie":"over18=1",  # 因為進入網站時會問是否滿18，而瀏覽器會用cookie:over18=1來表示滿18
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")  # 把網站資料讀取下來放入變數 data

    ## 解析原始碼，取得文章標題
    import bs4  # pip install beautifulsoup4

    root = bs4.BeautifulSoup(data, "html.parser")  # HTML格式去做解析
    titles = root.find_all("div", class_="title")  # .find_all 尋找所有 class  = "title" 的 div 標籤 (list type 形式)
    for title in titles:
        if title.a != None:  # 如果標題含有 a 標籤表示文章沒有被刪除，那就印出來
            print(title.a.string)  # title 代表 div 、 .a 代表 a 標籤 、 .string 表示取得a標籤裡的文字就好

    ## 抓取下一個頁面的連結
    nextLink = root.find("a", string="‹ 上頁")  # 找到內文是 ‹ 上頁 的a標籤
    # print(nextLink["href"])  # 印出下一個頁面的連結，並用["href"]取出連結
    return nextLink["href"]  # 回傳下一個頁面的連結

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3:
    url = "https://www.ptt.cc"+getURL(url)  # 覆蓋為新的url
    count += 1