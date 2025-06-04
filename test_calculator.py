from calculator import add, subtract, multiply, divide, power

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) == "Error: Division by zero"

def test_power():
    assert power(2, 3) == 8
