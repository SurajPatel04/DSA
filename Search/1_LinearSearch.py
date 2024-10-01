def linearSearch(arr, find):
    for i in arr:
        if i == find:
            return "Found", i
    
    return "Not Found"



arr = [1,2,3,4,5,11,10]
print(linearSearch(arr,2))
print(linearSearch(arr,111))