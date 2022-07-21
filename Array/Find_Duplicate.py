def duplicate(li):
    li = sorted(li)
    if len(li) <= 1:
        return 0
    for i in range(len(li)):
        if li[i+1]-li[i] == 0:
            return li[i]


li = [int(x) for x in input().split()]
print(duplicate(li))
