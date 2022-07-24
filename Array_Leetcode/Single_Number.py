def single_number(li):
    dict = {}
    for i in li:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in dict:
        if dict[i] == 1:
            return i


li = [int(x) for x in input().split()]
print(single_number(li))
