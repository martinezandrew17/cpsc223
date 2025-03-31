from functions import load_data, save_data, add_student, view_students

def main():
    filename = 'students.json'
    student_data = load_data(filename)

    while True:
        print("\n--- Student Data Management System ---")
        print("1. Add a new student")
        print('2. View all students')
        print("3. Save and exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_student(student_data)
        elif choice == '2':
            view_students(student_data)
        elif choice == '3':
            save_data(student_data, filename)
            print("Data saved successfully. Exiting the program.")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()