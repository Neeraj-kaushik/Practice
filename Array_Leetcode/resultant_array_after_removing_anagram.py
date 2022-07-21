def removedlist(li):
    def anagram(a, b):
        a = sorted(a)
        b = sorted(b)
        if a == b:
            return True
        else:
            return False
    li1 = []
    li1.append(li[0])
    for i in range(1, len(li)):
        if anagram(li[i], li1[-1]):
            continue
        else:
            li1.append(li[i])
    return li1


li = [x for x in input().split()]
print(removedlist(li))
