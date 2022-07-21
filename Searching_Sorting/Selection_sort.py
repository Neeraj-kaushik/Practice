def ssort(li):
    for i in range(len(li)-1):
        minindex = i
        for j in range(i+1, len(li)):
            if li[j] < li[minindex]:
                minindex = j
        li[i], li[minindex] = li[minindex], li[i]
    return li


li = [int(x) for x in input().split()]
print(ssort(li))
