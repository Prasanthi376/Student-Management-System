import sqlite3
import os

def create_table():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(

        roll INTEGER PRIMARY KEY,
        name TEXT,
        branch TEXT,
        age INTEGER,
        marks REAL

    )
    """)


    connection.commit()
    connection.close()



def save_student(student):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO students
        VALUES(?,?,?,?,?)
        """,
        (
            student.roll,
            student.name,
            student.branch,
            student.age,
            student.marks
        )
    )


    connection.commit()
    connection.close()



def load_students():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM students"
    )


    data = cursor.fetchall()


    connection.close()


    return data


def get_all_students():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    connection.close()

    return data



def get_student_by_roll(roll):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM students WHERE roll=?",
        (roll,)
    )


    data = cursor.fetchone()


    connection.close()


    return data



def update_student_data(roll, name, branch, age, marks):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE students
        SET name=?,
            branch=?,
            age=?,
            marks=?
        WHERE roll=?
        """,
        (
            name,
            branch,
            age,
            marks,
            roll
        )
    )


    connection.commit()

    updated = cursor.rowcount


    connection.close()


    return updated


def delete_student_data(roll):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        "DELETE FROM students WHERE roll=?",
        (roll,)
    )


    connection.commit()


    deleted = cursor.rowcount


    connection.close()


    return deleted


def count_all_students():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )


    count = cursor.fetchone()[0]


    connection.close()


    return count

def get_statistics():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    # Total students
    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    total = cursor.fetchone()[0]


    # Highest marks student
    cursor.execute(
        """
        SELECT name, marks
        FROM students
        ORDER BY marks DESC
        LIMIT 1
        """
    )

    highest = cursor.fetchone()


    # Lowest marks student
    cursor.execute(
        """
        SELECT name, marks
        FROM students
        ORDER BY marks ASC
        LIMIT 1
        """
    )

    lowest = cursor.fetchone()


    # Average marks
    cursor.execute(
        "SELECT AVG(marks) FROM students"
    )

    average = cursor.fetchone()[0]


    connection.close()


    return total, highest, lowest, average

def sort_students_by_roll():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM students ORDER BY roll"
    )


    data = cursor.fetchall()


    connection.close()

    return data



def sort_students_by_name():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM students ORDER BY name"
    )


    data = cursor.fetchall()


    connection.close()

    return data



def sort_students_by_marks():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM students ORDER BY marks DESC"
    )


    data = cursor.fetchall()


    connection.close()

    return data

import csv

def export_students_csv():

    students = get_all_students()

    if not students:
        return False


    with open("students_export.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Roll Number",
                "Name",
                "Branch",
                "Age",
                "Marks"
            ]
        )


        for student in students:

            writer.writerow(student)


    return True

