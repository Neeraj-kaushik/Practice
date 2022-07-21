def remove_duplicate(li):
    a = 0
    while a < len(li)-1:
        if li[a] == li[a+1]:
            li.pop(a+1)
            continue
        a += 1
    return li


li = [int(x) for x in input().split()]
print(remove_duplicate(li))
