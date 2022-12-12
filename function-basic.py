# 定義函式

# def multiply():  # 函式內部程式碼若是沒有做函式呼叫就不會執行
#     print(3*4)

# def multiply(n1, n2):  # 可之後再設定參數數字
#     print(n1*n2)

# def multiply(n1, n2):
#     print(n1*n2)  # 印出兩數相乘結果
#     return n1*n2  # 回傳兩數相乘結果

# 呼叫函式

# multiply()


# multiply(10, 8)


# value = multiply(3, 4)  # value 得到的回傳值為 12
# print(value)  # 印出 value


# practice

def calculate(max):  # 累加到指定數字
    sum = 0
    for i in range(1,max+1):
        sum += i
    print(sum)

calculate(10)
calculate(20)