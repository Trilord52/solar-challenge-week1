import pandas as pd

def load_data():
    """Load cleaned datasets from Google Drive URLs and concatenate them with a Country column."""
    try:
        # Direct download links from Google Drive
        benin_url = "https://drive.google.com/uc?export=download&id=1CpAf63iOj8xrdr87Zea3csJGjtJWshid"
        sierra_leone_url = "https://drive.google.com/uc?export=download&id=11ATWm6ITFXeVYNYJ_-QY55PPb1701ajF"
        togo_url = "https://drive.google.com/uc?export=download&id=19AlYUXK8FZ1ARQ_23MME2BJaAD4SRxOt"
        
        print("Loading Benin CSV...")
        benin_df = pd.read_csv(benin_url)
        print("Loading Sierra Leone CSV...")
        sierra_leone_df = pd.read_csv(sierra_leone_url)
        print("Loading Togo CSV...")
        togo_df = pd.read_csv(togo_url)

        benin_df['Country'] = 'Benin'
        sierra_leone_df['Country'] = 'Sierra Leone'
        togo_df['Country'] = 'Togo'

        combined_df = pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)
        combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp'])
        return combined_df
    except Exception as e:
        raise Exception(f"Failed to load data: {str(e)}")

def get_top_regions(df, metric='GHI', top_n=3):
    """Get top regions by average metric (e.g., GHI)."""
    avg_metric = df.groupby('Country')[metric].mean().sort_values(ascending=False)
    return avg_metric.head(top_n).reset_index()