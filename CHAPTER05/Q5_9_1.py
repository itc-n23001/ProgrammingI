mountains_in_japan = {"fuji": 3776, "kitadake": 3193, "okuhodakadake": 3190, "dummy": 0}
mountains_in_japan_sorted = sorted(
    mountains_in_japan.items(), key=lambda x: x[1], reverse=True
)
print(mountains_in_japan_sorted)
