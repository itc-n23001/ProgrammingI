for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# 実行結果↓
# 1
# 3
# 5
# 7
# 9
for x in range(10):
    if x % 2 == 0:
        break
    print(x)
