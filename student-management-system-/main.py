import json
import os

# File paths
STUDENT_FILE = "resources/student(1).json"
WELCOME_FILE = "resources/welcome.txt"
WELCOME2_FILE = "resources/Welcome2(1).txt"

def read_file(file_path):
    """Read and return the content of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return ""

def save_student_data(data):
    """Save student data to a JSON file."""
    # noinspection PyTypeChecker
    with open(STUDENT_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def load_student_data():
    """Load student data from a JSON file."""
    try:
        if os.path.exists(STUDENT_FILE):
            with open(STUDENT_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
    except json.JSONDecodeError:
        print("Error: JSON file is corrupted. Starting with an empty record.")
        return {}
    return {}


def add_student():
    """Add a new student."""
    students = load_student_data()
    print("\nAdd a new student:")
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Error: Student ID already exists.")
        return

    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    major = input("Enter student major: ").upper()

    students[student_id] = {"name": name, "phone": phone, "major": major}
    save_student_data(students)
    print("✔ Student added successfully!")

def display_students():
    """Display all students."""
    students = load_student_data()
    if not students:
        print("No students found.")
        return

    print("\nStudent Records:")
    for student_id, details in students.items():
        print(f"ID: {student_id}, Name: {details['name']}, Phone: {details['phone']}, Major: {details['major']}")

def delete_student():
    """Delete a student by ID."""
    students = load_student_data()
    student_id = input("Enter student ID to delete: ")
    if student_id not in students:
        print("Error: Student ID not found.")
        return

    confirm = input("Are you sure you want to delete this student? (y/n): ").lower()
    if confirm == 'y':
        del students[student_id]
        save_student_data(students)
        print("✔ Student deleted successfully!")
    else:
        print("Deletion canceled.")

def modify_student():
    """Modify a student's record."""
    students = load_student_data()
    student_id = input("Enter student ID to modify: ")
    if student_id not in students:
        print("Error: Student ID not found.")
        return

    print(f"Current record: {students[student_id]}")
    name = input("Enter new name (press Enter to skip): ") or students[student_id]['name']
    phone = input("Enter new phone (press Enter to skip): ") or students[student_id]['phone']
    major = input("Enter new major (press Enter to skip): ").upper() or students[student_id]['major']

    students[student_id] = {"name": name, "phone": phone, "major": major}
    save_student_data(students)
    print("✔ Student record updated successfully!")

def query_student():
    """Query a student's record by ID."""
    students = load_student_data()
    student_id = input("Enter student ID to query: ")
    if student_id not in students:
        print("Error: Student ID not found.")
        return

    print(f"Student record: {students[student_id]}")

def menu():
    while True:
        welcome_content = read_file(WELCOME_FILE)
        print(welcome_content)

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            modify_student()
        elif choice == "4":
            query_student()
        elif choice == "5":
            display_students()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    menu()