def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    dict = {}
    li1 = list(str1)
    li2 = list(str2)
    for i in li1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for i in li2:
        if i not in dict:
            return False
        dict[i] -= 1
        if dict[i] < 0:
            return False
    
    return True
    
arr = "car"
arr2= "rat"
print(anagram("anagram","nagaram"))
print(anagram(arr,arr2))

def test_anagram_function():
    print(anagram("listen", "silent")) # True
    print(anagram("conversation", "voices rant on")) # True
    print(anagram("Dormitory", "Dirty room"))
    print(anagram("hello", "world"))
    print(anagram("a!b@c", "c@b!a"))
    print(anagram("", ""))
    print(anagram("a", "a"))
    print(anagram("a", "b"))
    print(anagram("abc", "abcd"))

test_anagram_function()
