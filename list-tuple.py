# List
grades = [12, 60, 15, 70, 90]

# print(grades)  # 列印出list
# print(grades[0])  # 列印list索引值第 0 個

grades[0] = 55  # 將list中第 0 個資料更新為 55
# print(grades)
# print(grades[1:4])  # 將list中1~3個印出

grades = grades + [12, 33]  # 將新數值加入list
# print(grades)

length = len(grades)  # 取得列表長度
# print(length)

data = [[4, 5, 6, 7], [2, 4, 6, 7]]  # 巢狀烈表
# print(data)

data[0][0:2] = [1, 2]  # 更新data裡第0個裡的0~1
# print(data)

data[0][0:2] = [1, 2, 3]  # 更新data裡第0個裡的0~1,同時把3放進去
# print(data)

# Tuple 和 List 操作一模一樣,除了更新資料
x = (1, 2)
# x[0] = 2
# print(x)
