import streamlit as st
import pandas as pd

# Sample data (replace this with real data)
data = {
    "College Name": ["College A", "College B", "College C", "College D"],
    "State": ["State 1", "State 2", "State 1", "State 3"],
    "Exam": ["Exam 1", "Exam 2", "Exam 1", "Exam 3"],
    "Category": ["General", "OBC", "SC", "General"],
    "Quota": ["AI", "HS", "AI", "HS"],
    "Fees": [100000, 150000, 120000, 90000],
    "Branch": ["CS", "IT", "ME", "EE"],
    "Vacancy": [10, 5, 8, 7],
    "Percentile Required": [90, 85, 80, 95],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Streamlit app title
st.title("College Selection App")

# User inputs
exam_selected = st.selectbox("Select Exam", df["Exam"].unique())
state_selected = st.selectbox("Select State", df["State"].unique())
category_selected = st.selectbox("Select Category", df["Category"].unique())
quota_selected = st.selectbox("Select Quota", df["Quota"].unique())
percentile = st.slider("Select Your Percentile", 0, 100, 75)

# Filtering data based on user inputs
filtered_df = df[
    (df["Exam"] == exam_selected) &
    (df["State"] == state_selected) &
    (df["Category"] == category_selected) &
    (df["Quota"] == quota_selected) &
    (df["Percentile Required"] <= percentile)
]

# Display results
st.subheader("Matching Colleges")
st.write(filtered_df)

# Additional filters
max_fees = st.slider("Max Fees", 0, 200000, 150000)
filtered_df = filtered_df[filtered_df["Fees"] <= max_fees]
st.write(filtered_df)

branch_preference = st.multiselect("Select Branch Preferences", df["Branch"].unique())
if branch_preference:
    filtered_df = filtered_df[filtered_df["Branch"].isin(branch_preference)]
    st.write(filtered_df)

vacancy_required = st.slider("Minimum Branch Vacancy", 0, 20, 5)
filtered_df = filtered_df[filtered_df["Vacancy"] >= vacancy_required]
st.write(filtered_df)
