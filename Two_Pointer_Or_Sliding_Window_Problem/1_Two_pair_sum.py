# Given a Sorted array find the number pair which is equal to sum k

def pairSum(arr,k):
    left = 0
    right = len(arr) - 1
    result = []
    while left < right:
        if arr[left] + arr[right] < k:
            left += 1
        elif arr[left] + arr[right] > k:
            right -= 1
        else: 
            result.append([left, right])
            return result

arr = [1,2,3,4]
print(pairSum(arr,3))
                

