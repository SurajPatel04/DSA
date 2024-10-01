
def maxSubArray(nums):
    if not nums:
        return 0
    currentSum = nums[0]
    maxSum = nums[0]
    hold = currentSum
    for i in nums[1:]:
        currentSum = max(i, currentSum+i)
        maxSum = max(currentSum, maxSum)
        hold = currentSum
    return maxSum


# or 

def maxSubArray(self, nums):
        cu = 0
        mx = float('-inf')
        for i in nums:
            cu += i
            if cu > mx:
                mx= cu
            if cu < 0:
                cu = 0
        return mx

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubArray(arr))