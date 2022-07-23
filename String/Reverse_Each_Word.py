def reverse(s):
    x = s.split()
    li = [ele[::-1] for ele in x]
    return ' '.join(li)


s = input()
print(reverse(s))
