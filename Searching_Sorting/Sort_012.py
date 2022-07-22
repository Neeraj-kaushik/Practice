def sort_arr(li):
    x = 0
    m = len(li)-1
    i = 0
    while i <= m:
        if li[i] == 0:
            li[x], li[i] = li[i], li[x]
            x += 1
            i += 1
        elif li[i] == 2:
            li[m], li[i] = li[i], li[m]
            m -= 1
        else:
            i += 1
    return li


li = [int(x) for x in input().split()]
print(sort_arr(li))
