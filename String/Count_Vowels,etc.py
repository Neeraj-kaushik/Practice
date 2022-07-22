def count(s):
    v, c, x, n = 0, 0, 0, 0
    for i in s:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                v += 1
            else:
                c += 1
        elif(i >= '0' and i <= '9'):
            n += 1
        else:
            x += 1
    return v, c, x, n


s = input()
v, c, x, n = count(s)
print(v, c, x, n)
