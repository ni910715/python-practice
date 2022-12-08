# while 迴圈

n = 1
while n <= 3:  # n <= 3 執行迴圈裡程式碼
    print(n)  #印出現在的 n
    n += 1  # 每次都加 1

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

n = 1
sum = 0  # 紀錄累加結果
while n <= 10:
    sum += n
    n += 1
print(sum)

# for 迴圈

for x in [3, 4, 5]:  # list
    print(x)

for x in "hello":  # string
    print(x)

for x in range(10):
    print(x)

for x in range(5, 10):
    print(x)

    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

total = 0  # 紀錄累加結果
for x in range(1, 11):  # x 從 1 到 10
    total += x
# print(total)
