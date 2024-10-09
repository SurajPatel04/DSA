import pytest

# test/test_productOfElementExceptSelf.py
from my_array.problem.productElementExceptSelf import product



def test_product_except_self():
    assert product([1,2,3,4]) == [24,12,8,6]
    assert product([-1,0,1,2,3]) == [0,-6,0,0,0]
