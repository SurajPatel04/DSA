# def dublicate(arr):
#     dict = {}
#     arr1 = []
#     for i in arr:
#         if i not in dict:
#             dict[i] = True
#         else:
#             arr1.append(i)
        
#     return arr1


# def tolist(arr1, arr2):
#     dict = {}
#     common = []
#     for i in arr1:
#         dict[i] = True
    
#     for j in arr2:
#         if j in dict:
#             common.append(j)
        
#     return common

# arr = [1,2,4,5,2,1,2,1]
# arr2 = [1,2,44,3,4,2,1,10,2,11]


# print(tolist(arr,arr2))

# def first_non_repeating_char(string):
#     my_dict = {}
#     common = []
#     notCommon = []
#     for i in string:
#         if i not in my_dict:
#             my_dict[i] = True

#     return my_dict

# print( first_non_repeating_char('leetcode') )

# print( first_non_repeating_char('hello') )

# print( first_non_repeating_char('aabbcc') )



# """
#     EXPECTED OUTPUT:
#     ----------------
#     l
#     h
#     None

# """


def has_unique_chars(str):
    dict = {}
    hold = []
    for j in str:
        if j not in dict:
            dict[j] = True
        else:
            hold.append(j)
            
    
    if len(hold) == 0:
        return True
    else:
        return False
        



print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""