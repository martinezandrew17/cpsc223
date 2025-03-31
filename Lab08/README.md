# **Student Data Management System**  

## **Objective**  
The goal of this lab is to create a Python program that manages student data using file handling and JSON. The program will allow users to:  
- Add new student records.  
- View all student records.  
- Save the data to a JSON file.  

---

## **Requirements**  

### **1. Student Data Structure**  
Each student is represented as a dictionary with the following keys:  
- **"name"**: The student's name (string).  
- **"age"**: The student's age (integer).  

#### **Example:**  
```python
student_data = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 21},
]
```

---

### **2. Functions to Implement**  

#### **`load_data(filename)`**  
- Loads student data from a JSON file.  
- If the file doesn't exist, returns an empty list.  

#### **`save_data(data, filename)`**  
- Saves the student data to a JSON file.  

#### **`add_student(data)`**  
- Adds a new student record to the list after taking input from the user.  

#### **`view_students(data)`**  
- Displays all student records in a readable format.  

---

### **3. Main Program (`main.py`)**  
The `main.py` file will:  
1. Load student data from a JSON file (if it exists).  
2. Provide a menu for the user to:  
   - Add a new student.  
   - View all students.  
   - Save and exit.  

---

## **Files in the Lab**  

### **1. `functions.py`**  
Contains the implementation of the functions:  
- `load_data(filename)`  
- `save_data(data, filename)`  
- `add_student(data)`  
- `view_students(data)`  

### **2. `main.py`**  
The main program that loads data, provides a menu, and interacts with the user.  

### **3. `students.json`**  
The JSON file where student data is saved. This file is created automatically when the program runs for the first time.  

---

## **Steps to Complete the Lab**  

### **1. Implement the Functions**  
- Write the code for `load_data`, `save_data`, `add_student`, and `view_students` in `functions.py`.  

### **2. Write the Main Program**  
- Create the `main.py` file to load data, display the menu, and call the appropriate functions based on user input.  

### **3. Test the Program**  
- Run the program and test all the options (`add`, `view`, `save and exit`).  
- Check the `students.json` file to ensure the data is saved correctly.  

---

