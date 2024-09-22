def first_non_repeating_char(string):
    my_dict = {}
    hold = []
    dublicate = []
    for i in string:
        if i not in my_dict:
            my_dict[i] = i
            
            hold.append(i)
    
    return hold


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