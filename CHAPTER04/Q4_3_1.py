def concat_words(*args, separator="."):
    return separator.join(args)


s = concat_words(
    "vagrant@ubuntu", "-jammy", "~/ProgrammingI/", "CHAPTER04$", separator="_"
)
print(s)

# ターミナル上で今いるところを表示します。
