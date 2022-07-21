def max_pair(li):
    dic = {}
    ans = [0, 0]
    for i in li:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.values():
        ans[0] += i//2
        if i % 2 != 0:
            ans[1] += 1

    return ans


li = [int(x) for x in input().split()]
print(max_pair(li))
