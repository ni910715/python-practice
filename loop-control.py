# break

n = 0
while n < 5:
    if n == 3:
        break  # 如果為True 跳出迴圈
    print(n)
    n += 1
print("最後的 n: ", n)

# continue

n = 0
for x in [0, 1, 2, 3]:
    if x % 2 == 0:
        continue  # 直接執行下一個迴圈
    print(x)
    n += 1
print("最後的 n: ", n)

# else

sum = 0
for x in range(11):
    sum += x
else: # 結束迴圈前執行
    print(sum)

# practice 解整數平方根

n = int(input("請輸入一個正整數: "))
for i in range(n):
    if i*i == n:
        print("整數平方根為: ", i)
        break  # 如果是 break 結束迴圈，不會執行 else
else:
    print("沒有整數平方根")
