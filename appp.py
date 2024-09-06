import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import openpyxl
# File uploader widget
st.title("Finance Data Analysis and Visualization")
st.write("## Upload Your Dataset")
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_excel(uploaded_file)

    # Display the dataset
    st.write("## Dataset")
    st.dataframe(df)

    # Summary Statistics
    st.write("## Summary Statistics")
    st.write(df.describe())

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Handle any conversion issues

    # Check if the Date column conversion was successful
    if df['Date'].isnull().any():
        st.warning("There are invalid dates in your dataset. Please check the Date column.")
    
    # Plotting
    st.write("## Revenue, Expense, and Profit Trends")

    # Plot trends over time
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x='Date', y='Revenue', label='Revenue', ax=ax)
    sns.lineplot(data=df, x='Date', y='Expense', label='Expense', ax=ax)
    sns.lineplot(data=df, x='Date', y='Profit', label='Profit', ax=ax)
    ax.set_title('Trends Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Amount')
    ax.legend()
    st.pyplot(fig)

    # Bar chart for each day
    st.write("## Revenue, Expense, and Profit Comparison")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.set_index('Date')[['Revenue', 'Expense', 'Profit']].plot(kind='bar', ax=ax)
    ax.set_title('Daily Comparison of Revenue, Expense, and Profit')
    ax.set_xlabel('Date')
    ax.set_ylabel('Amount')
    st.pyplot(fig)

    # Pie chart for distribution
    st.write("## Distribution of Revenue, Expense, and Profit")
    fig, ax = plt.subplots(figsize=(8, 8))
    sizes = [df['Revenue'].sum(), df['Expense'].sum(), df['Profit'].sum()]
    labels = ['Total Revenue', 'Total Expense', 'Total Profit']
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title('Revenue, Expense, and Profit Distribution')
    st.pyplot(fig)
else:
    st.write("Please upload a dataset to get started.")
