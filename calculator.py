"""calculator"""

import math


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raise ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def run_tests() -> None:
    """boundary laboratory"""
    # Normal cases
    assert add(2, 3) == 5.0
    assert subtract(10, 4) == 6.0
    assert multiply(-3, 4) == -12.0
    assert divide(7, 2) == 3.5

    # Boundary cases
    assert math.isclose(add(0.1, 0.2), 0.3)  # float precision
    assert divide(0, 5) == 0.0               # zero numerator

    # Invalid case: division by zero must raise an error
    try:
        divide(5, 0)
        assert False, "divide(5, 0) should raise ZeroDivisionError"
    except ZeroDivisionError:
        pass

    print("All tests passed")


if __name__ == "__main__":
    run_tests()