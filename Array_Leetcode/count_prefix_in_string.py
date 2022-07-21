def count_prefix(li, s):
    count = 0
    for i in range(len(li)):
        a = len(li[i])
        if li[i] == s[0:a]:
            count += 1
    return count


li = [x for x in input().split()]
s = input()
print(count_prefix(li, s))
