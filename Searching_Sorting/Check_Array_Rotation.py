def rotation(li):
    if len(li) <= 1:
        return -1
    for i in range(len(li)):
        if li[i] > li[i+1]:
            return (i+1)
    return 0


li = [int(x) for x in input().split()]
print(rotation(li))
