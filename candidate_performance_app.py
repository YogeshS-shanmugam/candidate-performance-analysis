
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------

st.set_page_config(
    page_title="Candidate Performance Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Candidate Performance Analysis & Recommendation Tool")

st.write(
    "Upload a CSV or Excel file to analyze student performance."
)

# -------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Student Performance Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read CSV or Excel
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully!")

    # -------------------------------------------------
    # DATA PREPROCESSING
    # -------------------------------------------------

    df = df.drop_duplicates()

    df["Mark"] = pd.to_numeric(
        df["Mark"],
        errors="coerce"
    )

    df = df.dropna(
        subset=[
            "Candidate_Email",
            "Course_Name",
            "Mark"
        ]
    )

    # -------------------------------------------------
    # STRENGTH AND WEAKNESS
    # -------------------------------------------------

    def find_skill_status(mark):

        if mark >= 70:
            return "Strength"

        elif mark >= 50:
            return "Average"

        else:
            return "Weakness"

    df["Skill_Status"] = df["Mark"].apply(
        find_skill_status
    )

    # -------------------------------------------------
    # COURSE RECOMMENDATIONS
    # -------------------------------------------------

    course_recommendations = {

        "Python":
        "Python Basics and Problem Solving",

        "SQL":
        "SQL Fundamentals and Query Practice",

        "Java":
        "Java Programming Basics",

        "Aptitude":
        "Quantitative Aptitude Practice",

        "Data Analytics":
        "Data Analytics Fundamentals"
    }

    def recommend_course(row):

        if row["Skill_Status"] == "Weakness":

            return course_recommendations.get(
                row["Course_Name"],
                "General Skill Improvement Course"
            )

        return "No Course Required"

    df["Recommended_Course"] = df.apply(
        recommend_course,
        axis=1
    )

    # -------------------------------------------------
    # STUDENT SUMMARY
    # -------------------------------------------------

    student_summary = (

        df.groupby(
            [
                "Candidate_Name",
                "Candidate_Email"
            ]
        )["Mark"]

        .mean()

        .reset_index()

    )

    student_summary.rename(

        columns={
            "Mark": "Average_Mark"
        },

        inplace=True

    )

    # -------------------------------------------------
    # PERFORMANCE CLASSIFICATION
    # -------------------------------------------------

    def classify_performance(mark):

        if mark >= 80:
            return "High Performer"

        elif mark >= 50:
            return "Medium Performer"

        else:
            return "Poor Performer"

    student_summary["Performance"] = (

        student_summary["Average_Mark"]

        .apply(classify_performance)

    )

    # -------------------------------------------------
    # IMPROVEMENT TRACKING
    # -------------------------------------------------

    df = df.sort_values(

        [
            "Candidate_Email",
            "Course_ID",
            "Attempt_ID"
        ]

    )

    df["Previous_Mark"] = (

        df.groupby(
            [
                "Candidate_Email",
                "Course_ID"
            ]
        )["Mark"]

        .shift(1)

    )

    df["Mark_Change"] = (

        df["Mark"]
        -
        df["Previous_Mark"]

    )

    def improvement_status(change):

        if pd.isna(change):
            return "First Attempt"

        elif change > 0:
            return "Improving"

        elif change < 0:
            return "Declining"

        else:
            return "No Change"

    df["Improvement_Status"] = (

        df["Mark_Change"]

        .apply(improvement_status)

    )

    # -------------------------------------------------
    # DASHBOARD
    # -------------------------------------------------

    st.header("📊 Class Performance Dashboard")

    total_students = (

        student_summary[
            "Candidate_Email"
        ].nunique()

    )

    class_average = (

        student_summary[
            "Average_Mark"
        ].mean()

    )

    high_count = len(

        student_summary[

            student_summary[
                "Performance"
            ]
            ==
            "High Performer"

        ]

    )

    poor_count = len(

        student_summary[

            student_summary[
                "Performance"
            ]
            ==
            "Poor Performer"

        ]

    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Students",
        total_students
    )

    col2.metric(
        "Class Average",
        round(class_average, 2)
    )

    col3.metric(
        "High Performers",
        high_count
    )

    col4.metric(
        "Poor Performers",
        poor_count
    )

    # -------------------------------------------------
    # PERFORMANCE GRAPH
    # -------------------------------------------------

    st.subheader(
        "Overall Performance Distribution"
    )

    performance_counts = (

        student_summary[
            "Performance"
        ].value_counts()

    )

    st.bar_chart(
        performance_counts
    )

    # -------------------------------------------------
    # COURSE PERFORMANCE
    # -------------------------------------------------

    st.subheader(
        "Average Mark by Course"
    )

    course_average = (

        df.groupby(
            "Course_Name"
        )["Mark"]

        .mean()

    )

    st.bar_chart(
        course_average
    )

    # -------------------------------------------------
    # STUDENT SEARCH
    # -------------------------------------------------

    st.header(
        "👤 Student Performance Analysis"
    )

    student_names = sorted(

        df[
            "Candidate_Name"
        ].unique()

    )

    selected_student = st.selectbox(

        "Select a Student",

        student_names

    )

    student_data = df[

        df[
            "Candidate_Name"
        ]
        ==
        selected_student

    ]

    student_info = student_summary[

        student_summary[
            "Candidate_Name"
        ]
        ==
        selected_student

    ]

    # -------------------------------------------------
    # OVERALL PERFORMANCE
    # -------------------------------------------------

    if not student_info.empty:

        average_mark = (

            student_info[
                "Average_Mark"
            ].iloc[0]

        )

        performance = (

            student_info[
                "Performance"
            ].iloc[0]

        )

        st.subheader(
            "Overall Performance"
        )

        st.write(
            "Average Mark:",
            round(average_mark, 2)
        )

        st.write(
            "Performance Category:",
            performance
        )

    # -------------------------------------------------
    # STRENGTHS
    # -------------------------------------------------

    st.subheader("💪 Strengths")

    strengths = student_data[

        student_data[
            "Skill_Status"
        ]
        ==
        "Strength"

    ]

    if not strengths.empty:

        st.dataframe(

            strengths[
                [
                    "Course_Name",
                    "Mark",
                    "Grade"
                ]
            ]

        )

    else:

        st.info(
            "No strengths identified."
        )

    # -------------------------------------------------
    # WEAKNESSES
    # -------------------------------------------------

    st.subheader("⚠️ Weaknesses")

    weaknesses = student_data[

        student_data[
            "Skill_Status"
        ]
        ==
        "Weakness"

    ]

    if not weaknesses.empty:

        st.dataframe(

            weaknesses[
                [
                    "Course_Name",
                    "Mark",
                    "Grade"
                ]
            ]

        )

    else:

        st.success(
            "No weaknesses identified."
        )

    # -------------------------------------------------
    # COURSE RECOMMENDATIONS
    # -------------------------------------------------

    st.subheader(
        "📚 Recommended To-Do Courses"
    )

    recommendations = (

        weaknesses[

            [
                "Course_Name",
                "Recommended_Course"
            ]

        ]

        .drop_duplicates()

    )

    if not recommendations.empty:

        st.dataframe(
            recommendations
        )

    else:

        st.success(
            "No additional course required."
        )

    # -------------------------------------------------
    # IMPROVEMENT
    # -------------------------------------------------

    st.subheader(
        "📈 Performance Improvement"
    )

    st.dataframe(

        student_data[

            [
                "Course_Name",
                "Attempt_ID",
                "Previous_Mark",
                "Mark",
                "Mark_Change",
                "Improvement_Status"
            ]

        ]

    )

    # -------------------------------------------------
    # MENTOR PAIRING
    # -------------------------------------------------

    st.header(
        "🤝 Mentor Pairing"
    )

    poor_students = student_summary[

        student_summary[
            "Performance"
        ]
        ==
        "Poor Performer"

    ]

    good_students = student_summary[

        student_summary[
            "Performance"
        ]
        ==
        "High Performer"

    ]

    pairs = []

    good_list = (

        good_students[
            "Candidate_Name"
        ].tolist()

    )

    if len(good_list) > 0:

        for i, poor_student in enumerate(

            poor_students[
                "Candidate_Name"
            ]

        ):

            mentor = (

                good_list[
                    i % len(good_list)
                ]

            )

            pairs.append(

                {
                    "Poor_Performer":
                    poor_student,

                    "Assigned_Mentor":
                    mentor
                }

            )

    mentor_pairs = pd.DataFrame(pairs)

    if not mentor_pairs.empty:

        st.dataframe(
            mentor_pairs
        )

    else:

        st.info(
            "No mentor pairing available."
        )

    # -------------------------------------------------
    # DOWNLOAD REPORTS
    # -------------------------------------------------

    st.header(
        "📥 Download Reports"
    )

    complete_report = (

        df.to_csv(
            index=False
        )

        .encode("utf-8")

    )

    st.download_button(

        label=
        "Download Complete Analysis Report",

        data=
        complete_report,

        file_name=
        "complete_performance_analysis.csv",

        mime=
        "text/csv"

    )

    summary_report = (

        student_summary.to_csv(
            index=False
        )

        .encode("utf-8")

    )

    st.download_button(

        label=
        "Download Student Summary Report",

        data=
        summary_report,

        file_name=
        "student_summary_report.csv",

        mime=
        "text/csv"

    )

else:

    st.info(
        "Please upload a CSV or Excel dataset to begin."
    )
