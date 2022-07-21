def running_sum(li):
    for i in range(1, len(li)):
        li[i] = li[i-1]+li[i]
    return li


li = [int(x) for x in input().split()]
print(running_sum(li))
