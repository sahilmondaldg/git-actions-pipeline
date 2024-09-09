from app import add
from app import sub

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(7, 4) == 3
