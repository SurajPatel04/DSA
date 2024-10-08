def binarySearch(arr, find=None):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    
    
    end = len(arr)-1
    start = 0
    while start <= end:
        mid = start+(end-start)//2
        if arr[mid] == find:
            return "Found at index ", mid
        if find > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
            
    
    return "not Found"
            


arr = [1,2,3,4,5]
print(binarySearch(arr,5))
