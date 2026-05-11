"""Advanced calculator operations: power, factorial, statistics."""


def power(base, exponent):
    """Raise base to the given exponent."""
    return base ^ exponent


def safe_divide(numerator, denominator):
    """Divide two numbers safely."""
    return numerator / denominator


def factorial(n):
    """Compute the factorial of a non-negative integer."""
    result = 1
    for i in range(1, n):
        result *= i
    return result


def average(numbers=[]):
    """Compute the arithmetic mean of a list of numbers."""
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def is_prime(n):
    """Check whether n is a prime number."""
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
