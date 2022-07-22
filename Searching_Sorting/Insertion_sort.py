def isort(li):
    for i in range(1, len(li)):
        j = i-1
        temp = li[i]
        while j >= 0 and li[j] > temp:
            li[j+1] = li[j]
            j = j-1
        li[j+1] = temp
    return li


li = [int(x) for x in input().split()]
print(isort(li))
