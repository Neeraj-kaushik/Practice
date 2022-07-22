def merge_array(li1, li2):
    i, j, k = 0, 0, 0
    n = len(li1)
    m = len(li2)
    li3 = [0]*(n+m)
    while i < n and j < m:
        if li1[i] < li2[j]:
            li3[k] = li1[i]
            k += 1
            i += 1
        else:
            li3[k] = li2[j]
            k += 1
            j += 1
    while i < len(li1):
        li3[k] = li1[i]
        k += 1
        i += 1
    while j < len(li2):
        li3[k] = li2[j]
        k += 1
        j += 1
    return li3


li1 = [int(x) for x in input().split()]
li2 = [int(x) for x in input().split()]
print(merge_array(li1, li2))
