list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [x if x % 2 == 0 else None for x in list1]
print(list2)
