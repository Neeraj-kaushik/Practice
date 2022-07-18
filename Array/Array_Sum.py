def sum_array(nums):
    sum1 = 0
    for i in range(len(nums)):
        sum1 += nums[i]
    return sum1


nums = [int(x) for x in input().split()]
print(sum_array(nums))
