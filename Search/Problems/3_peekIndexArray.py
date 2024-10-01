def peek(arr):
    start = 0
    end = len(arr) -1
    result = -1
    while (start <= end):
        mid = start + (end -start) //2
        result = mid
        if arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
            end = mid -1
        elif arr[mid] < arr[mid+1]:
            start = mid + 1
        else:
            return result

def peekanother(arr):
    start = 0
    end = len(arr) -1
    result = -1
    mid = start + (end -start) //2
    while (start < end):
        if arr[mid] < arr[mid+1]:
            start = mid+1
        else:
            end = mid
            
        mid = start + (end -start) //2
        
    return mid
        
arr = [3,9,8,6,4]
print(peekanother(arr))
            
            