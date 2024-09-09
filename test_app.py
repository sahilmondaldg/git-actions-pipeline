from app import add, sub, mult, div

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(7, 4) == 3

def test_mult():
    assert mult(3, 4) == 12

def test_div():
    assert div(10, 2) == 5
