def majorityElement(arr):
    dict = {}   
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            
    print(max(dict, key=dict.get))
    print(dict)
    
print(majorityElement([1,1,2,2,2,3]))
print(majorityElement(["q","q","s","t"]))