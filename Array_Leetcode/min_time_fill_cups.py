def fillcups(li):
    count = 0
    while max(li) > 0:
        if li[0] < li[1]:
            li[0], li[1] = li[1], li[0]
        if li[1] < li[2]:
            li[1], li[2] = li[2], li[1]
        li[0], li[1] = li[0]-1, li[1]-1
        count += 1
    return count


li = [int(x) for x in input().split()]
print(fillcups(li))
