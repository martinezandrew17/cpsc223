import exceptions_lab as el

def main():
    # Test divide_numbers
    print("Testing divide_numbers:")
    print("5 / 2 =", el.divide_numbers(numerator=5, denominator=2))  # Expected: 2.5
    print("5 / 0 =", el.divide_numbers(numerator=5, denominator=0))  # Expected: Error message
    
    # Test parse_int
    print("\nTesting parse_int:")
    print("Parse '123':", el.parse_int(value="123"))  # Expected: 123
    print("Parse 'abc':", el.parse_int(value="abc"))  # Expected: Error message
    
    # Test custom_exception_demo
    print("\nTesting custom_exception_demo:")
    try:
        print("Value 5:", el.custom_exception_demo(value=5))  # Expected: 5
        print("Value -5:", el.custom_exception_demo(value=-10))  # Expected: Exception
    except el.NegativeValueError as e:
        print("NegativeValueError:", e)
    
    # Test chain_exception_demo
    print("\nTesting chain_exception_demo:")
    try:
        el.chain_exception_demo(filename="nonexistent_file.txt")
    except Exception as e:
        print("Caught exception:", e)
        print("Original exception:", e.__cause__)
    
    # Test cleanup_demo
    print("\nTesting cleanup_demo:")
    try:
        print(el.cleanup_demo(filename="test_file.txt"))  # Expected: Cleanup message printed
    except Exception as e:
        print("Exception occurred:", e)
    
    # Test type_error_demo
    print("\nTesting type_error_demo:")
    print("5 + 3:", el.type_error_demo(5, 3))  # Expected: 8
    print("5 + 'a':", el.type_error_demo(5, 'a'))  # Expected: Error message

if __name__ == "__main__":
    main()