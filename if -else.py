# if else 判斷式

x = input("請輸入數字: ")  # input輸入為string type
x = int(x)  # int()轉會為整數型態
if x > 200:
    print("大於 200")
elif x > 100:
    print("大於 100,小於 200")
else:
    print("小於 100")


# practice

num1 = int(input("請輸入第一個數字: "))
num2 = int(input("請輸入第二個數字: "))
op = input("請輸入 +, -, *, /: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("不支援運算")

# switch 目前都不支援

