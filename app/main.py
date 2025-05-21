import streamlit as st
import pandas as pd
from utils import SolarDataProcessor
from visualizations import plot_ghi_distribution

st.title("Solar Data Dashboard")  # Set the title of the Streamlit dashboard

# Initialize data processor and load data with error handling
processor = SolarDataProcessor()
try:
    df = processor.load_data()
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

st.subheader("Select Countries to Compare")  # Add a subheader for country selection
countries = df['Country'].unique().tolist()  # Get unique countries from the data
selected_countries = st.multiselect("Countries", countries, default=countries)  # Allow user to select countries

# Filter data based on user selection
filtered_df = df[df['Country'].isin(selected_countries)]

if not filtered_df.empty:  # Check if the filtered dataframe is not empty
    st.subheader("GHI Distribution by Country")  # Add a subheader for the plot
    fig = plot_ghi_distribution(filtered_df, selected_countries)  # Use modular plotting function
    st.pyplot(fig)  # Display the plot in Streamlit
else:
    st.warning("Please select at least one country to display the plot.")  # Warn user if no country is selected

st.subheader("Top Regions by Average GHI")  # Add a subheader for the table
try:
    top_regions = processor.get_top_regions(metric='GHI', top_n=3)  # Get top 3 regions with error handling
    st.table(top_regions)  # Display the table in Streamlit
except KeyError as e:
    st.error(f"Error processing regions: {str(e)}")