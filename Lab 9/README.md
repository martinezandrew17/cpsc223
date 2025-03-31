

# Lab: Errors and Exceptions in Python

## Program Instructions
1. Create a module named exceptions_lab.
     1. Function: divide_numbers
          * Parameters: Keyword parameters numerator and denominator.
          * Behavior:
               * Attempt to perform the division numerator / denominator.
               * Use a try/except block to catch a ZeroDivisionError.
               * If a ZeroDivisionError occurs, return the message "Error: Division by zero".
               * If no exception occurs, return the result of the division.

     2. Function: parse_int
          * Parameter: Keyword parameter value.
          * Behavior:
               * Attempt to convert value to an integer.
               * Use a try/except block to catch a ValueError.
               * If a ValueError occurs, return the message "Error: Invalid integer".
               * If conversion is successful, return the integer value.

     3. User-Defined Exception: NegativeValueError
          * Define a class named NegativeValueError that inherits from Exception.
          * Include an appropriate docstring explaining that negative values are not allowed.
          
     4. Function: custom_exception_demo
          * Parameter: Keyword parameter value.
          * Behavior:
               * If value is negative, raise a NegativeValueError with a descriptive message indicating that negative values are not allowed.
               * Otherwise, return the value.
     
     5. Function: chain_exception_demo
          * Parameter: Keyword parameter filename.
          * Behavior:
               * Attempt to open the file specified by filename in read mode.
               * If the file does not exist, catch the FileNotFoundError and raise a new Exception with the message "Chained Exception: File operation failed", using exception chaining (i.e., with the from keyword).

     6. Function: cleanup_demo
          * Parameter: Keyword parameter filename.
          * Behavior:
               * Attempt to open the file in write mode.
               * Use a try/finally block to ensure that a cleanup message "Cleanup complete" is printed regardless of whether an exception occurs.
               * If an exception is raised during the file operation, it should be propagated after executing the cleanup.

     7. Function: type_error_demo
          * Parameters: Two positional parameters.
          * Behavior:
               * Attempt to add these two parameters.
               * Use a try/except block to catch a TypeError.
               * If a TypeError occurs, return the message "Error: Incompatible types for addition".
               * If addition is successful, return the result.


2. Create a main driver program to meet the following requirements:
     1. Create a file named main.py.
     2. Import the exceptions_lab module.
     3. Call each function with appropriate test values to demonstrate exception handling:
          * For chain_exception_demo, pass a filename that does not exist to trigger the exception.
          * For cleanup_demo, observe that the cleanup message is printed regardless of any exceptions.
     4. Testing Your Functions:
          * For each function, write sample test cases that display the function’s input and output.
          * Use inline comments to explain the test case and the expected result.
     5. Execution Block:
          * Use the following block to ensure tests run only when the module is executed directly:

## Submission
Submit a zip file containing all the code files on Canvas.
Naming Convention: `CWID_LastName_Firstname.zip`
Your zipped folder should contain the following files:
```
                  | > exceptions_lab.py
                  | > main.py
                  | > test.py
                  | > test.sh (for UNIX-based systems)
                  | > win_test.bat (for Windows systems)
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below. Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|20|All required files are submitted|
|30|All unit tests passed|
