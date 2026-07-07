from operations import *


def show_menu():

    print("\n=================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Count Students")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Sort By Roll")
    print("8. Sort By Name")
    print("9. Sort By Marks")
    print("10. Student Statistics")
    print("11. Exit")



while True:


    show_menu()


    choice = input("Enter your choice: ")


    if choice == "1":

        add_student()


    elif choice == "2":

        view_students()


    elif choice == "3":

        count_students()


    elif choice == "4":

        search_student()


    elif choice == "5":

        update_student()


    elif choice == "6":

        delete_student()


    elif choice == "7":

        sort_by_roll()


    elif choice == "8":

        sort_by_name()


    elif choice == "9":

        sort_by_marks()


    elif choice == "10":

        student_statistics()


    elif choice == "11":

        print("\nThank you for using Student Management System!")

        break


    else:

        print("\nInvalid choice! Try again.")
