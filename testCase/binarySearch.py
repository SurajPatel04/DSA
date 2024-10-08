# Test cases using pytest
def test_binary_search_array():
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert binary_fn(foo, 69) == True
    assert binary_fn(foo, 1336) == False
    assert binary_fn(foo, 69420) == True
    assert binary_fn(foo, 69421) == False
    assert binary_fn(foo, 1) == True
    assert binary_fn(foo, 0) == False

