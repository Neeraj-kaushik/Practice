def h_o_c(s):
    n = 256
    count = [0]*256
    max1 = -1
    for i in s:
        count[ord(i)] += 1
    for j in range(n):
        if count[j] > max1:
            max1 = count[j]
            b = chr(j)
    return b


s = input()
print(h_o_c(s))
