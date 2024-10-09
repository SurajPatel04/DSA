def product(arr):
    result = [1]*len(arr)
    prefix = 1
    postfix = 1
    for i in range(len(arr)):
        result[i] = prefix
        prefix *= arr[i]

    for i in range(len(arr)-1,-1,-1):
        result[i] *= postfix
        postfix *=  arr[i]

    return result
