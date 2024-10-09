import pytest
from my_array.problem.add import add

def test_add():
    assert add(1,2) == 3
    assert add(2,3) == 5