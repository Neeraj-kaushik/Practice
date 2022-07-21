def pivot(li):
    rightsum = sum(li)
    leftsum = 0
    for i in range(len(li)):
        rightsum = rightsum-li[i]
        if leftsum == rightsum:
            return i
        leftsum += li[i]
    return -1


li = [int(x) for x in input().split()]
print(pivot(li))
