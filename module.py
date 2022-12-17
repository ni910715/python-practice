## 載入內建的 sys 模組並取得資訊

import sys as s  # 在程式碼中 將 sys 以 s 使用
import sys
print(sys.platform)
print(sys.maxsize)

print(s.platform)
print(s.maxsize)

##建立一個自己的模組並使用

import geometry

result = geometry.distance(1, 1, 5, 5)
print(result)

result = geometry.slope(1, 2, 5, 6)
print(result)

## 調整搜尋模組的路徑

import sys
print(sys.path)  # 印出模組搜尋路徑，並無 modules 路徑
sys.path.append("modules")  # 新增一個名叫 modules 的資料夾，將原有搜尋路徑中加入 modules
print("-----------------")
print(sys.path)  # 會在模組搜尋路徑後面看到多了一個 modules 路徑
print("-----------------")

import geometry  # 在這裡 problems 會出現錯誤但程式可以執行不須理會
result = geometry.distance(1, 1, 5, 5)
print(result)