from utils import calculate_grade
class Student:
    """
    Student class to store details of a single student.
    """

    def __init__(self, roll, name, branch, age, marks):
        self.roll = roll
        self.name = name
        self.branch = branch
        self.age = age
        self.marks = marks

    def display(self):
        print("------------------------------")
        print(f"Roll Number : {self.roll}")
        print(f"Name        : {self.name}")
        print(f"Branch      : {self.branch}")
        print(f"Age         : {self.age}")
        print(f"Marks       : {self.marks:g}")
        print(f"Grade       : {calculate_grade(self.marks)}")
        print("------------------------------")
        

