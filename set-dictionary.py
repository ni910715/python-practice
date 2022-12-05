# Set運算

s1 = {3, 4, 5}
# print(5 in s1)  # 如果5在s1這個set裡，印True
# print(6 in s1)  # 不存在印False
# print(5 not in s1)
# print(6 not in s1)

s2 = {3, 4, 5}
s3 = {4, 5, 6, 7}
s4 = s2 & s3  # & 交集 取兩個都有的
# print(s4)

s5 = s2 | s3  # | 聯集 全部不包含重複的
# print(s5)

s6 = s2 - s3  # - 差集 從 s2 中減去與 s3 重疊的部分
# print(s6)

s7 = s2 ^ s3  # ^ 反交集，取兩個集合中不重疊的部分
# print(s7)

s = set("hello")  # set(字串)，將字串裡每一字拆解成set不包括重複的
# print(s)
# print("h" in s)
# print("A" in s)

# Dictionary運算 key : value配對

dic = {"apple": "蘋果", "banana": "香蕉", "strawberry": "草莓"}

# print(dic["apple"])

dic["apple"] = "小蘋果"
# print(dic["apple"])

# print("apple" in dic)  # 判斷key是否存在
# print("apple" not in dic)

del dic["apple"]  # 刪除key，同時相對應的value也會被刪除
# print(dic)

dic1 = {x: x*2 for x in s1}  # 從lsit資料中產生字典
# print(dic1)