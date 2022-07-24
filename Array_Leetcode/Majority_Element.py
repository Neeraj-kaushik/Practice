def majority_element(li):
    li.sort()
    mid = (len(li)-1)//2
    return li[mid]


li = [int(x) for x in input().split()]
print(majority_element(li))
