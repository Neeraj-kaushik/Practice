def bsort(li):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li


li = [int(x) for x in input().split()]
print(bsort(li))
