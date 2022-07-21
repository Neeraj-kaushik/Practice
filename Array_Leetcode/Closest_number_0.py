def close(li):
    max1 = 100000
    x = 100000
    for i in li:
        curr_dist = abs(i)
        if curr_dist <= max1:
            if abs(i) == abs(x):
                x = max(i, x)
            elif abs(i) < abs(x):
                x = i
            max1 = curr_dist

    return x


li = [int(x) for x in input().split()]
print(close(li))
