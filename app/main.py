import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_top_regions
st.title("Solar Data Dashboard")

df = load_data()
st.subheader("Select Countries to Compare")
countries = df['Country'].unique().tolist()
selected_countries = st.multiselect("Countries", countries, default=countries)

filtered_df = df[df['Country'].isin(selected_countries)]

if not filtered_df.empty:
       st.subheader("GHI Distribution by Country")
       fig, ax = plt.subplots(figsize=(10, 6))
       sns.boxplot(x='Country', y='GHI', data=filtered_df, palette='Set2', ax=ax)
       plt.title('GHI Distribution by Country')
       plt.xlabel('Country')
       plt.ylabel('GHI (W/m²)')
       st.pyplot(fig)
else:
       st.warning("Please select at least one country to display the plot.")

st.subheader("Top Regions by Average GHI")
top_regions = get_top_regions(df, metric='GHI', top_n=3)
st.table(top_regions)