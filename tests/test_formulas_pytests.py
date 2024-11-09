import formulas    # The code to test

def test_sqrt():
    assert formulas.sqrt(9) == 3

def test_square():
    assert formulas.square(2) == 4

def test_increment():
    assert formulas.increment(4) == 5

def test_decrement():
    assert formulas.decrement(4) == 3

def test_fail_decrement():
    assert formulas.decrement(4) != 4
