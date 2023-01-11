## Point 實體物件設計: 平面座標點

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 定義實體方法
    def show(self):
        print(self.x, self.y)

    def distance(self, targetx, targety): # 計算兩點距離
        return ((self.x - targetx)**2 + (self.y - targety)**2)**0.5

p = Point(3, 4) # 建立實體物件
p.show() # 呼叫實體方法 
result = p.distance(0, 0) # targetx = 0 , targety = 0
print(result)

## File 實體物件設計: 包裝檔案讀取的程式

class File:
    # 初始化函式
    def __init__(self, name): # 檔案名稱
        self.name = name
        self.file = None # 尚未開啟的檔案
    # 建立實體方法
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()

# 讀取一個檔案
f1 = File("instance\data1.txt") # 建立實體物件
f1.open()
data = f1.read()
print(data)