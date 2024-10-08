def anagram(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    my_dict = {}
    for i in arr1:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for i in arr2:
        if i not in my_dict:
            return False
        my_dict[i] -= 1
        if my_dict[i] < 0:
            return False

    return True


# print(anagram("listen","silent"))
# print(anagram("dad","bad"))


def commonElement(arr1, arr2):
    result = []
    dict = {}
    for i in arr1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in arr2:
        if i in dict:
            result.append(i)
        dict[i] -= 1

    return result


print(commonElement([1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 3]))


def MaximumSubArray(arr):
    currentSum = 0
    maxSum = float("-inf")
    for i in range(len(arr)):
        currentSum = currentSum + arr[i]
        if currentSum > maxSum:
            maxSum = currentSum

        if currentSum < 0:
            currentSum = 0

    return maxSum


print(MaximumSubArray([2, 3, -8, 7, -1, 2, 3]))
print(MaximumSubArray([-2, -4]))
print(MaximumSubArray([5, 4, 1, 7, 8]))


def swap(nums):
    for i in range(len(nums) // 2):
        temp = nums[i * 2]
        nums[i * 2] = nums[(i * 2) + 1]
        nums[(i * 2) + 1] = temp

    return nums


print(swap([1, 2, 7, 8, 5]))
print(swap([1, 2, 7, 8, 5, 6]))


def MajorityElement(arr1):
    dict = {}
    result = 0
    for i in arr1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    result = max(dict, key=dict.get)
    return result


print(MajorityElement([1, 2, 2, 2, 3, 3]))


def buyAndSell(arr):
    sell = 0
    buy = float("inf")
    hold = 0
    for i in range(len(arr)):
        if arr[i] < buy:
            buy = arr[i]
        hold = arr[i] - buy

        sell = max(sell, hold)
    return sell


print(buyAndSell([7, 1, 5, 3, 6, 4]))


def topKelement(arr, k):
    my_dict = {}
    result = []
    for i in arr:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for i in range(k):
        result.append(max(my_dict, key=my_dict.get))
        del my_dict[max(my_dict, key=my_dict.get)]

    return result


print(topKelement([1, 1, 1, 2, 2, 3], 2))
