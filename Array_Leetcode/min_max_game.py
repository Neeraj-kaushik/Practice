def min_max(li):
    if len(li) == 1:
        return li[0]
    a = len(li)//2
    li1 = [0]*a
    for j in range(len(li1)):
        if j % 2 == 0:
            li1[j] = min(li[2*j], li[2*j+1])
        else:
            li1[j] = max(li[2*j], li[2*j+1])
    return min_max(li1)


li = [int(x) for x in input().split()]
print(min_max(li))
