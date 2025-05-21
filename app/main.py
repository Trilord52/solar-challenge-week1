import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_top_regions

st.title("Solar Data Dashboard")  # Set the title of the Streamlit dashboard

# Load the solar data using the utility function
df = load_data()
st.subheader("Select Countries to Compare")  # Add a subheader for country selection
countries = df['Country'].unique().tolist()  # Get unique countries from the data
selected_countries = st.multiselect("Countries", countries, default=countries)  # Allow user to select countries

# Filter the dataframe based on selected countries
filtered_df = df[df['Country'].isin(selected_countries)]

if not filtered_df.empty:  # Check if the filtered dataframe is not empty
    st.subheader("GHI Distribution by Country")  # Add a subheader for the plot
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axis for the plot
    sns.boxplot(x='Country', y='GHI', data=filtered_df, palette='Set2', ax=ax)  # Plot boxplot of GHI by country
    plt.title('GHI Distribution by Country')  # Set the plot title
    plt.xlabel('Country')  # Label the x-axis
    plt.ylabel('GHI (W/m²)')  # Label the y-axis
    st.pyplot(fig)  # Display the plot in Streamlit
else:
    st.warning("Please select at least one country to display the plot.")  # Warn user if no country is selected

st.subheader("Top Regions by Average GHI")  # Add a subheader for the table
top_regions = get_top_regions(df, metric='GHI', top_n=3)  # Get top 3 regions by average GHI
st.table(top_regions)  # Display the table in Streamlit