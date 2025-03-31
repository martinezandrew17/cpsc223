import unittest
import os
import exceptions_lab

class TestExceptionsLab(unittest.TestCase):
    
    def test_divide_numbers_success(self):
        self.assertEqual(exceptions_lab.divide_numbers(numerator=10, denominator=2), 5.0)
        
    def test_divide_numbers_zero_division(self):
        self.assertEqual(exceptions_lab.divide_numbers(numerator=10, denominator=0), "Error: Division by zero")
    
    def test_parse_int_valid(self):
        self.assertEqual(exceptions_lab.parse_int(value="100"), 100)
        
    def test_parse_int_invalid(self):
        self.assertEqual(exceptions_lab.parse_int(value="abc"), "Error: Invalid integer")
        
    def test_custom_exception_demo_positive(self):
        self.assertEqual(exceptions_lab.custom_exception_demo(value=10), 10)
        
    def test_custom_exception_demo_negative(self):
        with self.assertRaises(exceptions_lab.NegativeValueError):
            exceptions_lab.custom_exception_demo(value=-1)
    
    def test_chain_exception_demo(self):
        with self.assertRaises(Exception) as context:
            exceptions_lab.chain_exception_demo(filename="non_existent_file.txt")
        self.assertIn("Chained Exception: File operation failed", str(context.exception))
    
    def test_cleanup_demo(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            exceptions_lab.cleanup_demo(filename="temp_test.txt")
        finally:
            sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Cleanup complete", output)
        if os.path.exists("temp_test.txt"):
            os.remove("temp_test.txt")
    
    def test_type_error_demo_success(self):
        self.assertEqual(exceptions_lab.type_error_demo(5, 10), 15)
    
    def test_type_error_demo_failure(self):
        self.assertEqual(exceptions_lab.type_error_demo("hello", 10), "Error: Incompatible types for addition")

if __name__ == '__main__':
    unittest.main()