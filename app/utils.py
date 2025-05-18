import pandas as pd

def load_data():
    """Load cleaned datasets from Google Drive URLs and concatenate them with a Country column."""
    # Direct download links from Google Drive
    benin_url = "https://drive.google.com/file/d/1AdoQw57Mfq-B1IeNgX06mTydodKLHjSv/view?usp=sharing"
    sierra_leone_url = "https://drive.google.com/file/d/1Yt7dqNQvAOVJllMHvx-NvkfX1OVBNtBo/view?usp=sharing"
    togo_url = "https://drive.google.com/file/d/1Wl6fmSdZcrQ9gFGvew-Xa_S3akype40f/view?usp=sharing"

    benin_df = pd.read_csv(benin_url)
    sierra_leone_df = pd.read_csv(sierra_leone_url)
    togo_df = pd.read_csv(togo_url)

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