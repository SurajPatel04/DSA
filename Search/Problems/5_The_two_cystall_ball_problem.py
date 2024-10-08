# Given two crystal balls that will break if dropped from high enough distance, determine the exact spot in which it will break in the most optimized way.
import math
def find(arr):
    jump = math.floor(math.sqrt(len(arr)))
    at = 0
    for i in range(0,len(arr),jump):
        if arr[i]:
            break
        
        at = i        

    
    for j in range(at, i+1):
        if arr[j]:
            return j
    
    return -1


print(find([0,0,0,0,0,0,0,1,1,1,1]))
print(find([0,0,0,0,0,0,0,0,0,0,0]))
print(find([1,1,1,1]))
print(find([0,0,1,1,1]))
print(find([0,0,0,0,0,0]))
