import math_operations

def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    if operation == 'add':
        result = math_operations.add(a,b)
    elif operation == 'subtract':
        result == math_operations.subtract(a,b)
    elif operation == 'multiply':
        result == math_operations.multiply(a,b)
    elif operation == 'divide':
        result == math_operations.divide(a,b)
    else: 
        print("Invalid Operation")
        return
    
    if result is not None: 
        print("The result is {result}")
    else: 
        print("Cannot divide by zero.")

    if __name__ == "__main__":
        main()
