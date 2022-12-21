## 網路連線

import urllib.request as request

src = "https://web.mcu.edu.tw/"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8")
print(data)

## 串接、擷取公開資料

import urllib.request as request
import json
src = "	https://od.cdc.gov.tw/eic/NHI_Influenza_like_illness.json"  # 政府公開資料網 json 格式資料
with request.urlopen(src) as response:
    data = json.load(response) # 資料屬 json 型態，載入 json 模組做資料處理

with open("data.txt","w") as file:  # 寫入檔案， w 寫入模式
    for year in data:  # data 是一個字典
        file.write(year["年"]+"\n")  # 寫入key值為 年 的值