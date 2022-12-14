# 參數預設資料

def power(base, exp=0):  # 將 exp 預設為 0 若沒有給值的話用 exp = 0
    print(base ** exp)


power(3, 2)
power(4)  # 第二個值在沒有預設的情況下會error


# 使用參數名稱對應

def divide(n1, n2):
    print(n1/n2)


divide(2, 4)
divide(n2=10, n1=30)  # 不需要按照順序給值，可用 = 給值


# 無限參數資料

def avg(*ns):  # *(加變數名稱) 代表不確定會有幾筆資料傳進來，傳進來的值以 tuple 型態
    sum = 0
    for n in ns:
        sum += n
    print(sum/len(ns))


avg(2, 10, -2, 4, 6, -8)
