import csv
from student import Student
from utils import *
from database import *
import sqlite3

students = []
create_table()


def add_student():

    print("\n===== ADD STUDENT =====")

    roll = get_integer("Enter Roll Number: ")

    name = get_name("Enter Name: ")

    branch = get_branch("Enter Branch: ")

    age = get_age()

    marks = get_marks()


    student = Student(
        roll,
        name,
        branch,
        age,
        marks
    )


    try:

        save_student(student)

        print("\nStudent Added Successfully!\n")


    except sqlite3.IntegrityError:

        print("\nRoll Number already exists!\n")


def view_students():

    data = get_all_students()

    return data


    for data in students_data:


        student = Student(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4]
        )


        student.display()

def count_students():

    total = count_all_students()


    print("\n===== TOTAL STUDENTS =====")

    print(f"Total Students: {total}")

def search_student():

    roll = get_integer("Enter Roll Number: ")


    data = get_student_by_roll(roll)


    if data is None:

        print("\nStudent not found.\n")
        return


    student = Student(
        data[0],
        data[1],
        data[2],
        data[3],
        data[4]
    )


    print("\n===== STUDENT FOUND =====")

    student.display()


def update_student():

    roll = get_integer("Enter Roll Number to Update: ")


    data = get_student_by_roll(roll)


    if data is None:

        print("Student not found.")
        return


    print("\n===== UPDATE STUDENT DETAILS =====")


    name = get_name("Enter New Name: ")

    branch = get_branch("Enter New Branch: ")

    age = get_age()

    marks = get_marks()


    result = update_student_data(
        roll,
        name,
        branch,
        age,
        marks
    )


    if result:

        print("\nStudent Updated Successfully!\n")

    else:

        print("\nUpdate failed.\n")

def delete_student():

    roll = get_integer("Enter Roll Number to Delete: ")


    data = get_student_by_roll(roll)


    if data is None:

        print("\nStudent not found.\n")
        return


    result = delete_student_data(roll)


    if result:

        print("\nStudent Deleted Successfully!\n")

    else:

        print("\nDelete failed.\n")

def export_to_csv():

    if not students:
        print("No students available.")
        return

    with open("students.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Header
        writer.writerow([
            "Roll Number",
            "Name",
            "Branch",
            "Age",
            "Marks",
            "Grade"
        ])

        # Student data
        for student in students:

            writer.writerow([
                student.roll,
                student.name,
                student.branch,
                student.age,
                student.marks,
                calculate_grade(student.marks)
            ])

    print("\nStudents exported successfully to students.csv\n")

def sort_by_roll():

    print("\n===== SORTED BY ROLL =====\n")

    data = sort_students_by_roll()

    display_student_list(data)

def sort_by_name():

    print("\n===== SORTED BY NAME =====\n")

    data = sort_students_by_name()

    display_student_list(data)

def sort_by_marks():

    print("\n===== SORTED BY MARKS =====\n")

    data = sort_students_by_marks()

    display_student_list(data)

    
def get_integer(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Please enter a valid integer.")


def get_float(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Please enter a valid float.")

def get_name(message):
    while True:
        name = input(message).strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name should contain only letters.")
            continue

        return name.title()


def get_age(message="Enter Age: "):
    while True:
        age = get_integer(message)   # reuse your integer helper
        if age > 0:
            return age
        else:
            print("Age must be greater than 0.")


def get_marks(message="Enter Marks: "):
    while True:
        marks = get_float(message)   # reuse your float helper
        if 0 <= marks <= 100:
            return marks
        else:
            print("Marks must be between 0 and 100.")

def get_branch(message):
    while True:
        branch = input(message).strip().upper()

        if branch == "":
            print("Branch cannot be empty.")
            continue

        if not branch.isalpha():
            print("Branch should contain only letters.")
            continue

        return branch

def student_statistics():

    total, highest, lowest, average = get_statistics()


    if total == 0:
        print("No students available.")
        return


    print("\n==============================")
    print("    STUDENT STATISTICS")
    print("==============================")


    print(f"Total Students : {total}")


    print(f"Highest Marks  : {highest[1]}")
    print(f"Topper         : {highest[0]}")


    print(f"Lowest Marks   : {lowest[1]}")
    print(f"Lowest Student : {lowest[0]}")


    print(f"Average Marks  : {average:.2f}")

def filter_by_branch():

    if not students:
        print("No students available.")
        return

    branch = get_branch("Enter Branch: ")

    matching_students = [
        student for student in students
        if student.branch == branch
    ]

    if not matching_students:
        print(f"\nNo students found in {branch} branch.\n")
        return

    print(f"\n===== {branch} STUDENTS =====\n")

    for student in matching_students:
        student.display()

    print(f"\nTotal {branch} Students: {len(matching_students)}\n")


def display_student_list(data):

    if not data:
        print("No students available.")
        return


    for row in data:

        student = Student(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )

        student.display()
