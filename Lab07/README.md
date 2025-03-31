# Lab 6: Python Modules and Packages

## Instructions:

### **Step 1: Create a Python Module**

1. Create a Python module named `math_operations.py` with the following functions:

   - `add(a, b)`: Returns the sum of `a` and `b`.
   - `subtract(a, b)`: Returns the difference between `a` and `b`.
   - `multiply(a, b)`: Returns the product of `a` and `b`.
   - `divide(a, b)`: Returns the quotient of `a` divided by `b`. If `b` is zero, return `None`.
2. Create a script named `main_math_operations.py` to interact with the `math_operations` module:

   - Prompt the user to input two numbers and an operation (add, subtract, multiply, divide).
   - Call the appropriate function from `math_operations.py` and display the result.

---

### **Step 2: Create a Python Package**

1. Create a Python package named `shapes` with the following structure:
   shapes/
   init.py
   circle.py
   rectangle.py
   triangle.py
2. Implement the following in each module:

- **`circle.py`**:
  - `area(radius)`: Returns the area of a circle.
  - `circumference(radius)`: Returns the circumference of a circle.
- **`rectangle.py`**:
  - `area(length, width)`: Returns the area of a rectangle.
  - `perimeter(length, width)`: Returns the perimeter of a rectangle.
- **`triangle.py`**:
  - `area(base, height)`: Returns the area of a triangle.
  - `perimeter(side1, side2, side3)`: Returns the perimeter of a triangle.

3. Create a script named `main_shapes.py` to interact with the `shapes` package:

- Prompt the user to choose a shape (circle, rectangle, triangle).
- Based on the user's choice, prompt for the required inputs (e.g., radius, length, width).
- Call the appropriate functions from the `shapes` package and display the results.

---

### **Step 3: Use `__all__` in a Package**

1. Modify the `shapes/__init__.py` file to include an `__all__` list:

```python
__all__ = ["circle", "rectangle"]
- This ensures that only the circle and rectangle modules are imported when from shapes import * is used.

2. Create a script named main_all.py to test the __all__ feature:
- Use from shapes import * and demonstrate that only the circle and rectangle modules are imported.

Submission Guidelines:
Submit all Python files (modules, packages, and scripts) in a single zip file.

Naming Convention: CWID_LastName_Firstname.zip.

Your zipped folder should contain the following files:
> math_operations.py
> main_math_operations.py
> shapes/ (with all submodules and __init__.py)
> main_shapes.py
> main_all.py
> test.py (unit testing file for grading)
> README.txt
> test.sh (for UNIX-based systems)
> win_test.bat (for Windows systems)
```
