import json
import os


def load_data(filename):
    """
    Loads student data from a JSON file.
    If the file doesn't exist, returns an empty list.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_data(data, filename):
    """
    Saves the student data to a JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_student(data):
    """
    Adds a new student record to the list after taking input from the user.
    """
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    student = {"name": name, "age": age}
    data.append(student)
    print(f"Student {name} added successfully!")


def view_students(data):
    """
    Displays all student records in a readable format.
    """
    if not data:
        print("No student records found.")
    else: 
        print("\nStudent Records:")
        for index, student in enumerate(data, start = 1):
            print(f'{index}. Name: {student['name']}, Age: {student['age']}')