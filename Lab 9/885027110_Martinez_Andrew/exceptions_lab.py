class NegativeValueError(Exception): # Class definition
    """Exception raised for negative
    values when they are not allowed."""
    pass

def divide_numbers(*, numerator, denominator):
    """Divide two numbers with exception handling for zero division."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero"
    
def parse_int(*, value):
    """Convert value to integer with exception handling for invalid input."""
    try:
        return int(value)
    except ValueError:
        return "Error: Invalid integer"
    
def custom_exception_demo(*, value):
    """Demonstrate custom exception for negative values."""
    if value < 0:
        raise NegativeValueError("Negative values are not allowed")
    return value


def chain_exception_demo(*, filename):
    """Demonstrate exception chaining when file is not found."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        raise Exception("Chained Exception: File operation failed") from e

def cleanup_demo(*, filename):
    """Demonstrate cleanup with finally block."""
    file = None
    try:
        file = open(filename, 'w')
        # Some file operations
        return "File operation successful"
    finally:
        print("Cleanup complete")
        if file:
            file.close()
        pass

def type_error_demo(param1, param2):
    """Demonstrate handling TypeError for incompatible addition."""
    try:
        return param1 + param2
    except TypeError:
        return "Error: Incompatible types for addition"




