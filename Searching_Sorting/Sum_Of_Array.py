def sum_arr(li, li1, n, m):
    x = 1+max(m, n)
    out = [0]*x
    y = max(m, n)
    i = n-1
    j = m-1
    carry = 0
    while i >= 0 and j >= 0:
        sum1 = li[i]+li1[j]+carry
        out[y] = sum1 % 10
        carry = sum1//10
        j -= 1
        i -= 1
        y -= 1
    while i >= 0:
        sum1 = li[i]+carry
        out[y] = sum1 % 10
        carry = sum1//10
        i -= 1
        y -= 1
    while j >= 0:
        sum1 = li1[j]+carry
        out[y] = sum % 10
        carry = sum1//10
        j -= 1
        y -= 1
    out[0] = carry
    return out


li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
n = len(li)
m = len(li1)
print(sum_arr(li, li1, n, m))
