import pandas as pd
def load_data():
       """Load cleaned datasets and concatenate them with a Country column."""
       benin_df = pd.read_csv("../data/processed/benin-malanville_clean.csv")
       sierra_leone_df = pd.read_csv("../data/processed/sierraleone-bumbuna_clean.csv")
       togo_df = pd.read_csv("../data/processed/togo_dapaong_qc_clean.csv")

       benin_df['Country'] = 'Benin'
       sierra_leone_df['Country'] = 'Sierra Leone'
       togo_df['Country'] = 'Togo'

       combined_df = pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)
       combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp'])
       return combined_df

def get_top_regions(df, metric='GHI', top_n=3):
       """Get top regions by average metric (e.g., GHI)."""
       avg_metric = df.groupby('Country')[metric].mean().sort_values(ascending=False)
       return avg_metric.head(top_n).reset_index()