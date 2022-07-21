def bsearch(li, x):
    start = 0
    end = len(li)-1
    while start <= end:
        mid = (start+end)//2
        if li[mid] == x:
            return mid
        elif li[mid] < x:
            start = mid+1
        elif li[mid] > x:
            end = mid-1
    return 0


li = [int(x) for x in input().split()]
x = int(input())
print(bsearch(li, x))
