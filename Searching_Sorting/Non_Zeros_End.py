def zero_end(li):
    x = 0
    for i in range(len(li)):
        if li[i] != 0:
            temp = li[x]
            li[x] = li[i]
            li[i] = temp
            x += 1
    return li


li = [int(x) for x in input().split()]
print(zero_end(li))
