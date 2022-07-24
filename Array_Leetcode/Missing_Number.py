def missing(li):
    li.sort()
    for i in range(len(li)-1):
        if li[i+1]-li[i] > 1:
            return (li[i+1]+li[i])//2
    return li[-1]+1


li = [int(x) for x in input().split()]
print(missing(li))
