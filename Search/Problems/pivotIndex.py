# def pivot(arr):
#     s = 0
#     e = len(arr)-1
#     mid = s + (e-s)//2
#     while(s<=e):
#         mid = s + (e-s)//2
#         if mid == len(arr)-1:
#             return mid
#         if arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]:
#             return mid
#         elif arr[mid] == arr[mid+1] and arr[mid] == arr[mid-1]:
#             e = mid-1
#         elif arr[mid] > arr[mid + 1]:
#             s = mid + 1
#         elif arr[mid] > arr[mid-1]:
#             e = mid - 1
                   

def pivot(arr):
    s =0
    e = len(arr)-1
    mid = s + (e-s)//2
    while(s<e):
        mid = s + (e-s)//2
        if arr[mid] > arr[e]:
            s= mid + 1
        else:
            e = mid
        
    return s

print(pivot([3,8,10,17,1]))
print(pivot([2,1,-1]))
print(pivot([1,2,-1]))
print(pivot([2,3,-1,8,4]))
