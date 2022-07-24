def contain(li):
    li.sort()
    for i in range(len(li)-1):
        if li[i+1]-li[i] == 0:
            return True
    return False


li = [int(x) for x in input().split()]
if contain(li):
    print('true')
else:
    print('false')
