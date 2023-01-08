## 定義類別與屬性

class IO:
    supportedSrcs = ["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read from",src)

## 使用類別  
# 使用方法:類別名稱.屬性名稱

# print(IO.supportedSrcs) 
# IO.read("file") # 將"file"給 read 裡的 src
input = input("請輸入讀取方式, console or file? ")
IO.read(input)  # 執行def read