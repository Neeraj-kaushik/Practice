from sys import stdin


def second_largest(li):
    if len(li) <= 1:
        return -2147483348
    largest = li[0]
    second = -2147483648
    for i in range(1, len(li)):
        if li[i] > largest:
            second = largest
            largest = li[i]
        elif second < li[i] and li[i] != largest:
            second = li[i]
    return second


li = [int(x) for x in input().split()]
print(second_largest(li))
