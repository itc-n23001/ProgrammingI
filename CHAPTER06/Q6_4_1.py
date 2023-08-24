# 意味わからなくてできませんでした。でも教科書に書いてたやつはすべてやりました

import random

random.seed(1)
msgs = [
    "Hi",
    "Hello",
    "Good morning",
    "Good night",
    "See you later",
    "How are you",
    "Have a good day",
]
with open("some.txt", "w") as f:
    for i in range(100000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))
f = open("some.txt")
c = 0
for u in f:
    print(u, end="")
    if c == 2:
        break
    c += 1
f.close()
