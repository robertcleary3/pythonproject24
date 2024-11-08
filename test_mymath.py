import mymath

def test_mymath_add():
    assert mymath.add_three(1,2, 3) == 3

def test_mymath_sub():
    assert mymath.subtract_three(8, 2, 1) == 5

def test_mymath_multiply():
    assert mymath.multiply_three(8, 2, 1) == 24

def test_mymath_divide():
    assert mymath.divide_three(8, 2, 1) == 2.6666666666666665

def test_mymath_square():
    assert mymath.square(9) == 81

def test_mymath_cube():
    assert mymath.cube(5) == 125