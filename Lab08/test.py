import unittest
import os
import json
from unittest.mock import patch
from functions import load_data, save_data, add_student, view_students

class TestStudentDataManager(unittest.TestCase):
    def setUp(self):
        # Create a temporary JSON file for testing
        self.test_filename = "test_students.json"
        self.test_data = [
            {"name": "Alice", "age": 20},
            {"name": "Bob", "age": 21},
        ]
        with open(self.test_filename, 'w') as file:
            json.dump(self.test_data, file, indent=4)

    def tearDown(self):
        # Clean up: Delete the temporary JSON file after testing
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_load_data_existing_file(self):
        # Test loading data from an existing file
        data = load_data(self.test_filename)
        self.assertEqual(data, self.test_data)

    def test_load_data_nonexistent_file(self):
        # Test loading data from a nonexistent file
        nonexistent_file = "nonexistent.json"
        data = load_data(nonexistent_file)
        self.assertEqual(data, [])

    def test_save_data(self):
        # Test saving data to a file
        new_data = [{"name": "Charlie", "age": 22}]
        save_data(new_data, self.test_filename)
        with open(self.test_filename, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, new_data)

    def test_add_student(self):
        # Test adding a new student
        data = []
        # Simulate user input
        with unittest.mock.patch('builtins.input', side_effect=["Charlie", "22"]):
            add_student(data)
        self.assertEqual(data, [{"name": "Charlie", "age": 22}])

    def test_view_students(self):
        # Test viewing students
        data = [{"name": "Alice", "age": 20}]
        # Capture the printed output
        with unittest.mock.patch('builtins.print') as mock_print:
            view_students(data)
            mock_print.assert_called_with("Name: Alice, Age: 20")

    def test_view_students_empty(self):
        # Test viewing an empty list of students
        data = []
        # Capture the printed output
        with unittest.mock.patch('builtins.print') as mock_print:
            view_students(data)
            mock_print.assert_called_with("No students found.")

if __name__ == '__main__':
    unittest.main()
