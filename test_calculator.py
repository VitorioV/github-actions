import pytest

from calculator import add, divide, is_even, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract() -> None:
    assert subtract(10, 4) == 6
    assert subtract(3, 5) == -2


def test_multiply() -> None:
    assert multiply(3, 4) == 12
    assert multiply(0, 99) == 0


def test_divide() -> None:
    assert divide(10, 2) == 5.0


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_is_even() -> None:
    assert is_even(4) is True
    assert is_even(7) is False