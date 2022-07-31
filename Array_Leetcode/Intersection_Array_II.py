def intersection(li, li1, li2):
    for i in li:
        if i not in li1:
            pass
        else:
            li2.append(i)
            li1.remove(i)
    return li2


li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
li2 = []
print(intersection(li, li1, li2))
