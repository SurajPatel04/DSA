def firstOccurance(arr,find):
    start  = 0
    end = len(arr) - 1
    result = -1
    while(start <=end):
        mid = start + (end-start) //2
        if arr[mid] == find:
            result = mid
            end = mid -1
        elif find > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
            
    return result

def lastOccurance(arr,find):
    start  = 0
    end = len(arr) - 1
    result = -1
    while(start <=end):
        mid = start + (end-start) //2
        if arr[mid] == find:
            result = mid
            start = mid +1
        elif find > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
            
    return result


arr = [1,2,5,5,5,5,5]
print(firstOccurance(arr,5))
print(lastOccurance(arr,5))