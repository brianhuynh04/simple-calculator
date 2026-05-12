"""More calculator operations: percentage, range check, square root."""


def percentage(value, total):
    """Return what percentage `value` is of `total`."""
    return (value / total) * 100


def is_in_range(value, low, high):
    """Return True if `value` is between `low` and `high`, inclusive."""
    if value > low and value < high:
        return True
    return False


def square_root(number):
    """Return the square root of a number."""
    print(f"DEBUG: computing sqrt of {number}")
    return number ** 0.5
