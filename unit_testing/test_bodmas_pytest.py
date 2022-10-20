from TestifyRepo.unit_testing import bodmas


def test_addition():
    assert bodmas.addition(3, 1) == 4
    assert bodmas.addition(5, 3) == 8
    assert bodmas.addition(30, 11) != 4
    assert bodmas.addition(5, 5) == 10


def test_subtraction():
    assert bodmas.subtraction(20, 10) == 10
    assert bodmas.subtraction(1, 2) == -1
    assert bodmas.subtraction(5, 7) != 30

