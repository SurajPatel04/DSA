def threePairSum(arr,sum):
    result = []
    for i in range(len(arr)-2):
        # Reset the set for each new first element
        seen = set()
        current_sum = sum - arr[i]
        for j in range(i+1, len(arr)):
            complement = current_sum - arr[j]
            if complement in seen:
                result.append(complement)
                result.append(arr[i])
                result.append(arr[j])
            seen.add(j)
            
    return result


arr = [1,2,3,4,5,6]
sum = 12

print(threePairSum(arr, sum))