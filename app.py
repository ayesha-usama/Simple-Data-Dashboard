
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write("Filtered Data:", filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)



    if st.button("Generate Plot"):
       st.write("Selected x-axis column:", x_column)
       st.write("Selected y-axis column:", y_column)
       st.write("Filtered Data Before Dropping NaN:", filtered_df)
       filtered_df = filtered_df.dropna(subset=[x_column, y_column])


       if x_column not in filtered_df.columns or y_column not in filtered_df.columns:
           st.error(f"Columns {x_column} and {y_column} must be selected")
           st.wtite("Available columns:", filtered_df.columns.tolist())
    else: 
        st.line_chart(filtered_df.set_index(x_column)[y_column])



