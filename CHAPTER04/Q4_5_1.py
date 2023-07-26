functions = [sum, min, max]
number_list = [1, 100]
for func in functions:
    print("Functions: {}, Result: {}".format(func.__name__, func(number_list)))
