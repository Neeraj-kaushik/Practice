def missing(li):
    N = len(nums)
    sumN = N * (N+1)
    sumN = sumN // 2

    csum = 0
    for i in nums:
        csum += i

    return sumN - csum


li = [int(x) for x in input().split()]
print(missing(li))
