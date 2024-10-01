def swap(arr):
    for i in range(len(arr)//2):
        temp = arr[i*2]
        arr[i*2] = arr[(i*2)+1]
        arr[(i*2)+1] = temp
        
    return arr


def anotherWay(arr):
    for i in range(0, len(arr) , 2):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        
    return arr


arr = [1,2,7,8,5]
arr1 = [1,2,7,8,5,6]
print
print(swap(arr))
print(arr1)
print(anotherWay(arr1))