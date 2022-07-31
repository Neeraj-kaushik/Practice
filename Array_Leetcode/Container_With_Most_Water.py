def container(li):
    max1 = 0
    l = 0
    r = len(li)-1
    while l < r:
        area = (r-l)*min(li[l], li[r])
        max1 = max(area, max1)
        if li[r] < li[l]:
            r -= 1
        else:
            l += 1
    return max1


li = [int(x) for x in input().split()]
print(container(li))
