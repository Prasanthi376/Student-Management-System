import streamlit as st
import matplotlib.pyplot as plt
import sqlite3

from student import Student


from database import (
    create_table,
    save_student,
    get_all_students,
    get_student_by_roll,
    update_student_data,
    delete_student_data,
    sort_students_by_roll,
    sort_students_by_name,
    sort_students_by_marks,
    get_statistics,
    export_students_csv
)

create_table()

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓"
)


st.title("🎓 Student Management System")
st.sidebar.success("Choose an operation")

st.sidebar.title("Menu")


choice = st.sidebar.selectbox(
    "Select Operation",
    [
        "Add Student",
        "View Students",
        "Search Student",
        "Update Student",
        "Delete Student",
        "Sort Students",
        "Statistics",
        "Export CSV",
        "Dashboard"
    ]
)


# ================= ADD STUDENT =================

if choice == "Add Student":

    st.header("➕ Add Student")

    roll = st.number_input(
        "Roll Number",
        min_value=1,
        step=1
    )

    name = st.text_input("Name")

    branch = st.text_input("Branch")

    age = st.number_input(
        "Age",
        min_value=1,
        step=1
    )

    marks = st.number_input(
        "Marks",
        min_value=0.0,
        max_value=100.0
    )

    if st.button("Add Student"):

        if name.strip() == "" or branch.strip() == "":

            st.warning("Please fill all fields.")

        else:

            student = Student(
                int(roll),
                name.title(),
                branch.upper(),
                int(age),
                float(marks)
            )

            try:

                save_student(student)

                st.success("✅ Student Added Successfully!")

            except sqlite3.IntegrityError:

                st.error("Roll Number already exists.")

            except Exception as e:

                st.error(str(e))


# ================= VIEW STUDENTS =================

elif choice == "View Students":

    st.header("📋 All Students")

    students = get_all_students()

    if not students:

        st.warning("No students found.")

    else:

        for s in students:

            with st.container():

                st.markdown(f"""
### 👨‍🎓 Roll Number: {s[0]}

**Name:** {s[1]}

**Branch:** {s[2]}

**Age:** {s[3]}

**Marks:** {s[4]}
""")

                st.divider()


                
# ================= SEARCH STUDENT =================

elif choice == "Search Student":

    st.header("🔍 Search Student")


    


    roll = st.number_input(
        "Enter Roll Number",
        min_value=1,
        step=1
    )


    if st.button("Search"):


        student = get_student_by_roll(roll)


        if student:


            st.success("Student Found")


            st.write(
                f"""
                ### Roll Number: {student[0]}

                **Name:** {student[1]}

                **Branch:** {student[2]}

                **Age:** {student[3]}

                **Marks:** {student[4]}
                """
            )


        else:

            st.error("Student not found")


# ================= UPDATE STUDENT =================

elif choice == "Update Student":

    st.header("✏️ Update Student")


    roll = st.number_input(
        "Enter Roll Number",
        min_value=1
        
    )


    if st.button("Load Student"):

        student = get_student_by_roll(roll)


        if student:

            st.session_state.student = student

            st.success("Student Loaded")


        else:

            st.error("Student not found")



    if "student" in st.session_state:


        student = st.session_state.student


        name = st.text_input(
            "Name",
            value=student[1]
        )


        branch = st.text_input(
            "Branch",
            value=student[2]
        )


        age = st.number_input(
            "Age",
            value=student[3]
        )


        marks = st.number_input(
            "Marks",
            min_value=0.0,
            max_value=100.0,
            value=float(student[4])
        )


        if st.button("Update Student"):


            result = update_student_data(
                roll,
                name,
                branch,
                age,
                marks
            )


            if result:

                st.success(
                    "Student Updated Successfully"
                )

                del st.session_state.student


            else:

                st.error(
                    "Update failed"
                )


# ================= DELETE STUDENT =================

elif choice == "Delete Student":

    st.header("🗑 Delete Student")


    roll = st.number_input(
        "Enter Roll Number to Delete",
        min_value=1
    )


    if st.button("Check Student"):


        student = get_student_by_roll(roll)


        if student:

            st.warning(
                f"""
                Student Found

                Roll: {student[0]}
                Name: {student[1]}
                Branch: {student[2]}
                Marks: {student[4]}
                """
            )

            st.session_state.delete_confirm = True


        else:

            st.error("Student not found")



    if "delete_confirm" in st.session_state:


        if st.button("Confirm Delete"):


            result = delete_student_data(int(roll))


            if result:

                st.success(
                    "Student Deleted Successfully"
                )

                del st.session_state.delete_confirm


            else:

                st.error(
                    "Delete failed"
                )


# ================= SORT STUDENTS =================

elif choice == "Sort Students":

    st.header("🔃 Sort Students")


    option = st.selectbox(
        "Sort By",
        [
            "Roll Number",
            "Name",
            "Marks"
        ]
    )


    if st.button("Sort"):


        if option == "Roll Number":

            students = sort_students_by_roll()


        elif option == "Name":

            students = sort_students_by_name()


        else:

            students = sort_students_by_marks()



        if students:


            for s in students:

                st.write(
                    f"""
                    ### Roll Number: {s[0]}

                    **Name:** {s[1]}

                    **Branch:** {s[2]}

                    **Age:** {s[3]}

                    **Marks:** {s[4]}
                    """
                )

                st.divider()


        else:

            st.warning("No students available")


# ================= STATISTICS =================

elif choice == "Statistics":

    st.header("📊 Student Statistics")


    total, highest, lowest, average = get_statistics()


    # Display total students

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Total Students",
            total
        )


    with col2:

        st.metric(
            "Average Marks",
            round(average,2) if average else 0
        )



    st.divider()



    if highest:

        st.subheader("🏆 Highest Marks")


        st.write(
            f"""
            **Student:** {highest[0]}

            **Marks:** {highest[1]}
            """
        )



    if lowest:

        st.subheader("📉 Lowest Marks")


        st.write(
            f"""
            **Student:** {lowest[0]}

            **Marks:** {lowest[1]}
            """
        )


# ================= EXPORT CSV =================

elif choice == "Export CSV":

    st.header("📤 Export Student Data")


    if st.button("Export"):

        result = export_students_csv()


        if result:

            st.success(
                "Students exported successfully!"
            )

            with open("students_export.csv","rb") as file:

                st.download_button(
                    label="Download CSV",
                    data=file,
                    file_name="students_export.csv",
                    mime="text/csv"
                )


        else:

            st.warning(
                "No students available"
            )


# ================= DASHBOARD =================

elif choice == "Dashboard":

    st.header("📊 Student Dashboard")


    students = get_all_students()


    if not students:

        st.warning("No data available")


    else:

        # -------- Marks Chart --------

        names = []
        marks = []


        for s in students:

            names.append(s[1])
            marks.append(s[4])


        st.subheader("Marks Overview")


        fig, ax = plt.subplots()


        ax.bar(
            names,
            marks
        )


        ax.set_xlabel("Students")
        ax.set_ylabel("Marks")
        ax.set_title("Student Marks")


        st.pyplot(fig)



        # -------- Branch Count --------


        st.subheader("Branch Distribution")


        branch_count = {}


        for s in students:

            branch = s[2]


            if branch in branch_count:

                branch_count[branch] += 1

            else:

                branch_count[branch] = 1



        fig2, ax2 = plt.subplots()


        ax2.pie(
            branch_count.values(),
            labels=branch_count.keys(),
            autopct="%1.1f%%"
        )


        ax2.set_title(
            "Students by Branch"
        )


        st.pyplot(fig2)
    
