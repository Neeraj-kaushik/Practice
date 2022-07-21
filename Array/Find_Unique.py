def unique(li):
    for i in range(len(li)):
        j = 0
        while j < len(li):
            if i != j:
                if li[i] == li[j]:
                    break
            j += 1
        if j == len(li):
            return li[i]


li = [int(x) for x in input().split()]
print(unique(li))
