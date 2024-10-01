def pairSum(arr, sum):
    result = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] + arr[j] == sum:
                result.append(min(arr[i],arr[j]))
                result.append(max(arr[i],arr[j]))
            
    return result


# Time Complexity O(n)
def pair(arr,sum):
    result = []
    seen = set()
    for i in arr:
        complement = sum - i
        if complement in seen:
            result.append(complement)
            result.append(i)
        seen.add(i)
        
    return result
            


arr = [1,2,3,4,5]
sum = 5
print(pairSum(arr,sum))
print(pair(arr,sum))