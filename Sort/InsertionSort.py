def Insertion(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while temp < arr[j] and j > -1:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
            
    return arr


print(Insertion([0,4,2,6,7,1,9]))