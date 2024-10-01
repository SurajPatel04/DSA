# Time Complexity O(n) and Space Complexity O(n)
def findDuplicate(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    maxElement = max(dict,key=dict.get)
    return maxElement


# Time Complexity O(n) and Space Complexity O(1)
def Floyds_Cycle_Detection(nums):
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow2 = 0
    while True:
        slow= nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            break
    
    return slow
arr = [10,10,11]

print(findDuplicate(arr))
print(Floyds_Cycle_Detection(arr))