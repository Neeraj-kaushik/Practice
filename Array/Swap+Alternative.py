def swap(li):
    for i in range(0, len(li)-1, 2):
        li[i], li[i+1] = li[i+1], li[i]
    return li


li = [int(x) for x in input().split()]
print(swap(li))
