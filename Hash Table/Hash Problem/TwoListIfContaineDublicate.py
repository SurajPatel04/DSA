# First Way With Big O(n^2)
# Steps:
# First Create function and pass argument
# Then start too for loop and compare two list

def items_in_commons_normal_way(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False



# Second Way Big O(2n) ==> O(n)
# Steps:
# First create funciton and pass argument
# Then create empty dict
# Start for loop and store list1 value in the dict
# Then again start for loop and compare list2 value with dict

def hash_way(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1,2,5]
list2 = [4,3,5]
print(items_in_commons_normal_way(list1,list2))
print(hash_way(list1, list2))