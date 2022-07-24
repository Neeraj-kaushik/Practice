def remove_duplicate(s):
    seen = s[0]
    ans = s[0]
    for i in s[1:]:
        if i != seen:
            ans += i
            seen = i
    return ans


s = input()
print(remove_duplicate(s))
