def intersection(li, li1):
    li2 = []
    for i in range(len(li)):
        for j in range(len(li1)):
            if li[i] == li1[j]:
                if li[i] not in li2:
                    li2.append(li[i])
    return li2


li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
print(intersection(li, li1))
