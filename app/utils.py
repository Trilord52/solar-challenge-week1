import pandas as pd

def load_data():
    """Load cleaned datasets from Google Drive URLs and concatenate them with a Country column."""
    try:
        # Direct download links from Google Drive for each country's data
        benin_url = "https://drive.google.com/uc?export=download&id=1CpAf63iOj8xrdr87Zea3csJGjtJWshid"
        sierra_leone_url = "https://drive.google.com/uc?export=download&id=11ATWm6ITFXeVYNYJ_-QY55PPb1701ajF"
        togo_url = "https://drive.google.com/uc?export=download&id=19AlYUXK8FZ1ARQ_23MME2BJaAD4SRxOt"
        
        print("Loading Benin CSV...")  # Indicate the start of Benin data loading
        benin_df = pd.read_csv(benin_url)  # Load Benin data
        print("Loading Sierra Leone CSV...")  # Indicate the start of Sierra Leone data loading
        sierra_leone_df = pd.read_csv(sierra_leone_url)  # Load Sierra Leone data
        print("Loading Togo CSV...")  # Indicate the start of Togo data loading
        togo_df = pd.read_csv(togo_url)  # Load Togo data

        benin_df['Country'] = 'Benin'  # Add country label to Benin data
        sierra_leone_df['Country'] = 'Sierra Leone'  # Add country label to Sierra Leone data
        togo_df['Country'] = 'Togo'  # Add country label to Togo data

        combined_df = pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)  # Combine all dataframes
        combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp'])  # Convert Timestamp to datetime
        return combined_df  # Return the combined dataframe
    except Exception as e:
        raise Exception(f"Failed to load data: {str(e)}")  # Raise an exception if loading fails

def get_top_regions(df, metric='GHI', top_n=3):
    """Get top regions by average metric (e.g., GHI)."""
    avg_metric = df.groupby('Country')[metric].mean().sort_values(ascending=False)  # Calculate average metric per country
    return avg_metric.head(top_n).reset_index()  # Return top N regions