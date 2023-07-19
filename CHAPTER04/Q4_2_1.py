def s(num=0):
    if num == 0:
        day = "today"
    elif num == 1:
        day = "tomorrow"
    elif num == -1:
        day == "yestday"
    else:
        day = "weekend"
    return day


j = s(num=1)
print(j)
