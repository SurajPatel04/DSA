def first_non_repeating_char(string):
    my_dict = {}
    hold = ""
    dublicate = []
    for i in string:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for i in string:
        if my_dict[i] == 1:
            return i
        
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
