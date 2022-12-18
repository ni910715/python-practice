## 儲存檔案

# open("檔案名稱", mode="開啟模式",encoding="編碼")

# file = open("data.txt", mode="w",encoding="utf-8")  # 開啟 加入 encoding="utf-8" 才可這常顯示中文，否則出現亂碼
# file.write("hello! file\nsecond line\n這是中文") # 操作 \n 可跳行
# file.close() # 關閉 釋放資源

##最佳實務寫法

# with open("檔案名稱",mode="開啟模式",encoding="編碼") as 檔案物件:

# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("hello! file\nsecond line\n這是最佳實務寫法")  # 不須使用 .close 來關閉檔案

# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n5")

# 讀取檔案 (已經存在的檔案)

# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data = file.read()
# print(data)

# sum = 0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file:  # 一行一行讀取
#         sum += int(line)
# print(sum)

## JSON 格式讀取、複寫檔案

# import json
# with open("config.json",mode="r",encoding="utf-8") as file:
#     data = json.load(file) # 從 json 讀取資料放入 data
# print(data)  # data 是一個字典型態
# data["name"] = "new name"  # 修改資料

# 把最新的資料副寫進去 json 檔案中

# with open("config.json",mode= "w") as file:
#     json.dump(data,file)