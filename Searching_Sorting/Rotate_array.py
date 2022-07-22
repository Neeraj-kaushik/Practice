def rotate_array(li, d):
    x = 1
    while x <= d:
        temp = li[0]
        for i in range(len(li)-1):
            li[i] = li[i+1]
        li[len(li)-1] = temp
        x += 1
    return li


li = [int(x) for x in input().split()]
d = int(input())
print(rotate_array(li, d))
