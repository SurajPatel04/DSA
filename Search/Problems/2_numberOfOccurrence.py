def firstOccurrence(arr, find):
    start = 0
    end = len(arr) - 1
    result = -1
    while (start<=end):
        mid = start + (end -start) // 2
        if arr[mid] == find:
            result = mid
            end = mid - 1
        elif find > arr[mid]:
            start = mid + 1
        else:
            end = mid-1
    
    return result

def lastOccurrence(arr, find):
    start = 0
    end = len(arr) - 1
    result = -1
    while (start <= end):
        mid = start + (end - start) // 2
        if arr[mid] == find:
            result = mid
            start = mid + 1
        elif find > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
            
    return result

def occurrence(arr, find):
    first = firstOccurrence(arr,find)
    last = lastOccurrence(arr, find)
    result = (last - first) + 1
    return result


arr = [1,2,3,4,5,6]
find = 5
print(occurrence(arr,find))