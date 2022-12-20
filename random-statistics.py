## 隨機模組(random)

import random
data = random.choice([1, 5, 6, 10, 20])  # 從 lsit 中隨機選取一個
print("現在的data: ",data)
data = random.sample([1, 5, 6, 10, 20], 3)  # 可以從 list 中自訂取出幾個值，但不能大於 list 本身
print("現在的data: ",data)

# 隨機調換順續
data = [1, 5, 8, 20]
random.shuffle(data) # 將 list 中的資料順序隨機調換，修改 list 本身
print("現在的data: ",data) 

#隨機取得亂數

data = random.random() # 只能 0 ~ 1 之間的隨數
print("現在的data: ",data)

data = random.uniform(10, 100)  # 可指定頭跟尾的隨機取數
print("現在的data: ",data)

#取得常態分配亂數 random.normalvariate( 平均數, 標準差 )
data = random.normalvariate(100, 10)  # 多數會在 90 ~ 110 之間
print("現在的data: ",data)

## 統計模組(statistics)

import statistics as stat

data = stat.mean([1, 2, 3, 4, 5, 8, 100])  # 取平均數
print("平均數: ",data)

data = stat.median([1, 2, 3, 4, 5, 8, 100])  # 取得中位數，可避免資料受極端值影響
print("中位數: ",data)

data = stat.stdev([1, 2, 3, 4, 5, 8, 10])  # 取得標準差
print("標準差: ",data)