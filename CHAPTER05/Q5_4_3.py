tp1 = (1, 2, 3, 4, 5)
tp2 = (1, 2, 3, 4, 5)
[x + y for (x, y) in zip(tp1, tp2)]


def tpadd(x, y):
    return x + y


list(map(tpadd, tp1, tp2))

# 出力するとどちらも同じ答え
