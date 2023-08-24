with open("my_math.py", "w") as f:
    f.write(
        """def my_pow(x, y):
    return x ** y\n"""
    )
import my_math

print(my_math.my_pow(2, 5))

print(my_math.my_pow(2, 0.5))

ans = my_math.my_pow(-4, 0.5)
print(ans)

print("実数成分: {}, 虚数成分: {}".format(ans.real, ans.imag))
