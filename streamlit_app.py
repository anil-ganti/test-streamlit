import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page title
st.title('Data Visualization Dashboard')

# Load data
@st.cache_data  # This caches the data loading
def load_data():
    # Replace 'your_data.csv' with your actual CSV file
    df = pd.read_csv('your_data.csv')
    return df

try:
    df = load_data()

    # Sidebar for filters
    st.sidebar.header('Filters')
    
    # Example: Create a year filter if your data has a year column
    if 'year' in df.columns:
        years = sorted(df['year'].unique())
        selected_years = st.sidebar.multiselect('Select Years', years, default=years)
        df_filtered = df[df['year'].isin(selected_years)]
    else:
        df_filtered = df

    # Display raw data option
    if st.sidebar.checkbox('Show Raw Data'):
        st.subheader('Raw Data')
        st.write(df_filtered)

    # Create visualizations
    st.subheader('Data Visualizations')

    # Example 1: Line Plot
    if 'date' in df.columns and 'value' in df.columns:
        st.subheader('Time Series Plot')
        fig1 = px.line(df_filtered, 
                      x='date', 
                      y='value',
                      title='Values Over Time')
        st.plotly_chart(fig1)

    # Example 2: Bar Chart
    if 'category' in df.columns and 'value' in df.columns:
        st.subheader('Category Analysis')
        fig2 = px.bar(df_filtered.groupby('category')['value'].mean().reset_index(),
                     x='category',
                     y='value',
                     title='Average Value by Category')
        st.plotly_chart(fig2)

    # Example 3: Scatter Plot
    if 'x_value' in df.columns and 'y_value' in df.columns:
        st.subheader('Correlation Plot')
        fig3 = px.scatter(df_filtered,
                         x='x_value',
                         y='y_value',
                         color='category' if 'category' in df.columns else None,
                         title='X vs Y Values')
        st.plotly_chart(fig3)

    # Example 4: Pie Chart
    if 'category' in df.columns:
        st.subheader('Distribution')
        fig4 = px.pie(df_filtered,
                      names='category',
                      values='value' if 'value' in df.columns else None,
                      title='Distribution by Category')
        st.plotly_chart(fig4)

except Exception as e:
    st.error(f"Error loading or processing data: {str(e)}")

    
