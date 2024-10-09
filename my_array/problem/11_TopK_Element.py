
# Time complexity is O(n*K)
def find_K_Element(arr, k):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    result = []

    for i in range(k):
        result.append(max(dict, key=dict.get))
        del dict[max(dict, key=dict.get)]
    return result


# You can use Heap

arr = [1,2,2,2,2,3,3,3]
k=2
print(find_K_Element(arr,k))
