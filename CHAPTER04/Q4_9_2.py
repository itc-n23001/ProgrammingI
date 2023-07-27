import os
import sys

MAX = 2
print(sys.getdefaultencoding())
print(os.path.baseneme(os.getcwd()))
for i in range(3):
    if MAX > i:
        print(MAX)
    else:
        print("#")
