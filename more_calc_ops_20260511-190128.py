"""More calculator operations: averaging, percent adjustment, halving."""


def compute_average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def add_one_percent(x):
    """Add one percent to x."""
    return x + 1


def half(x):
    """Return half of x."""
    return x // 2
