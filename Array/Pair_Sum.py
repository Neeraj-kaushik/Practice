def count(li, x):
    count = 0
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i]+li[j] == x:
                count += 1
    return count


li = [int(x) for x in input().split()]
x = int(input())
print(count(li, x))
