def plus_one(li):
    s = [str(i) for i in li]
    m = ''.join(s)
    print(m)
    k = int(m)
    k = k+1
    li = []
    while k != 0:
        rem = k % 10
        li.append(rem)
        k = k//10
    li = li[::-1]
    return li


li = [int(x) for x in input().split()]
print(plus_one(li))
