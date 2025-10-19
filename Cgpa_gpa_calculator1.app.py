import streamlit as st

st.set_page_config(page_title="CGPA Calculator")
st.title("🎓 CGPA & Grade Calculator")
st.write("Enter your subject marks for each semester to calculate your GPA and overall CGPA.")

# Ask for total number of semesters
semesters = st.number_input("Enter total number of semesters completed:", min_value=1, step=1)

semester_gpas = []
semester_credits = []

# Loop for each semester
for i in range(int(semesters)):
    st.header(f"Semester {i+1}")

    subjects = 6  # fixed number of subjects per semester
    subject_grades = []
    subject_credits = []

    for j in range(subjects):
        st.subheader(f"Subject {j+1}")
        mark = st.number_input(f"Enter marks (0–100) for Subject {j+1} (Semester {i+1}):",
                               min_value=0.0, max_value=100.0, step=1.0, key=f"mark_{i}_{j}")
        credit = st.number_input(f"Credit hours for Subject {j+1}:", min_value=0.5, step=0.5, value=3.0, key=f"credit_{i}_{j}")

        # Convert marks to GPA scale
        if mark >= 85:
            gpa = 4.0
            grade = "A+"
        elif mark >= 80:
            gpa = 3.7
            grade = "A"
        elif mark >= 75:
            gpa = 3.5
            grade = "B+"
        elif mark >= 70:
            gpa = 3.0
            grade = "B"
        elif mark >= 65:
            gpa = 2.5
            grade = "C+"
        elif mark >= 60:
            gpa = 2.0
            grade = "C"
        elif mark >= 50:
            gpa = 1.5
            grade = "D"
        else:
            gpa = 0.0
            grade = "F"

        st.caption(f"GPA for Subject {j+1}: **{gpa:.2f}** | Grade: **{grade}**")

        subject_grades.append(gpa)
        subject_credits.append(credit)
        st.divider()

    total_credits = sum(subject_credits)
    if total_credits > 0:
        sem_gpa = sum(g * c for g, c in zip(subject_grades, subject_credits)) / total_credits
        st.success(f"Semester {i+1} GPA: **{sem_gpa:.2f}**")
        semester_gpas.append(sem_gpa)
        semester_credits.append(total_credits)
    else:
        st.warning(f"Please enter valid credits for Semester {i+1}.")

# Calculate CGPA
if semester_credits:
    overall_cgpa = sum(g * c for g, c in zip(semester_gpas, semester_credits)) / sum(semester_credits)
    st.balloons()
    st.markdown(f"### 🎯 Overall CGPA: **{overall_cgpa:.2f}**")

    # Display grade according to CGPA
    if overall_cgpa >= 3.7:
        final_grade = "A"
    elif overall_cgpa >= 3.3:
        final_grade = "B+"
    elif overall_cgpa >= 3.0:
        final_grade = "B"
    elif overall_cgpa >= 2.5:
        final_grade = "C+"
    elif overall_cgpa >= 2.0:
        final_grade = "C"
    else:
        final_grade = "F"

    st.markdown(f"### 🏅 Final Grade: **{final_grade}**")
