def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divides a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
