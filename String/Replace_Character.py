def replace1(s, d, v):
    x = ""
    for i in s:
        if i != d:
            x += i
        else:
            x += v
    return x


s = input()
d = input()
v = input()
print(replace1(s, d, v))
