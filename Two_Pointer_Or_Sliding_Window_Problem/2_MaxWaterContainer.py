def maxWater(heights):
    left = 0
    right = len(heights) - 1
    hold = 0
    largest = 0
    while left < right:
        number = right - left
        hold = min(heights[left], heights[right]) * number
        if hold > largest:
            largest = hold

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return largest


print(maxWater([1, 7, 2, 5, 4, 7, 3, 6]))
print(maxWater([2, 2, 2]))
