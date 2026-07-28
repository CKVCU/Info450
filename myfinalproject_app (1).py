
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load data
cps_df = pd.read_csv("cps_project_data.csv")

# Data cleaning and feature engineering (as done in the notebook)
cps_df['UHRSWORKT'] = cps_df['UHRSWORKT'].replace([0, 997, 999], np.nan)

conditions = [
    (cps_df['EDUC'] >= 2) & (cps_df['EDUC'] <= 71),
    (cps_df['EDUC'] == 73),
    (cps_df['EDUC'] == 81),
    (cps_df['EDUC'] >= 91) & (cps_df['EDUC'] <= 92),
    (cps_df['EDUC'] == 111),
    (cps_df['EDUC'] >= 123) & (cps_df['EDUC'] <= 125)
]

choices = [
    'Less than High School',
    'High School Diploma',
    'Some College',
    'Associate Degree',
    "Bachelor's Degree",
    'Graduate Degree'
]
cps_df['EDUC_GROUP'] = np.select(conditions, choices, default='Other/Unknown')

cps_df['SEX_LABEL'] = np.where(cps_df['SEX'] == 1, 'Male', 'Female')

st.title("Weekly Earnings Analysis by Education and Gender")
st.sidebar.header("Filters")

# Interactive widgets
selected_education = st.sidebar.selectbox(
    "Select Education Group",
    options=cps_df['EDUC_GROUP'].unique().tolist()
)

selected_sex = st.sidebar.radio(
    "Select Sex",
    options=cps_df['SEX_LABEL'].unique().tolist()
)

# Filter data based on selections
filtered_df = cps_df[
    (cps_df['EDUC_GROUP'] == selected_education) &
    (cps_df['SEX_LABEL'] == selected_sex)
]

# Display filtered data or relevant insights
st.write(f"### Analysis for {selected_sex} with {selected_education}")

if not filtered_df.empty:
    avg_weekly_earnings = filtered_df['EARNWEEK2'].mean()
    st.write(f"Average Weekly Earnings: **${avg_weekly_earnings:.2f}**")

    st.subheader("Distribution of Weekly Earnings")
    fig = px.histogram(filtered_df, x="EARNWEEK2", nbins=50, title="Weekly Earnings Distribution")
    st.plotly_chart(fig)

    st.subheader("First 5 rows of Filtered Data")
    st.dataframe(filtered_df.head())
else:
    st.write("No data available for the selected filters.")
