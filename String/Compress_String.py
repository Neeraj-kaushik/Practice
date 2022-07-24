def compress(s):
    x = ''
    i = 0
    while i < len(s):
        c = 1
        j = i+1
        while j < len(s) and (s[j] == s[i]):
            j += 1
            c += 1
        if c == 1:
            x += s[i]
        else:
            x += s[i]+str(c)
        i = j
    return x


s = input()
print(compress(s))
