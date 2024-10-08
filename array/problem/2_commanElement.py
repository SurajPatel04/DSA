def common(arr1, arr2):
    dict = {}
    result = []
    for i in arr1:
        if i in dict:
            dict[i]  += 1
        else:
            dict[i] = 1
            
    for i in arr2:
        if i in dict and dict[i] > 0 :
            result.append(i)
            dict[i] -= 1
    
    
    return result


arr = [1,2,2,2,3,4]
arr2 =[10,2,2,3,3]

print(common(arr, arr2))