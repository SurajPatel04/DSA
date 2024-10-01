def unique(arr):
    ans = 0
    for i in range(len(arr)):
        ans = ans^arr[i]
    return ans

arr = [1, 2, 2, 3, 3]
print(unique(arr))
