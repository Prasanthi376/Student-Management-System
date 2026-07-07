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

def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"
