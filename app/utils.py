import pandas as pd

class SolarDataProcessor:
    """Class to handle solar data loading and processing."""
    
    def __init__(self):
        """Initialize the processor with an empty data attribute."""
        self.data = None

    def load_data(self):
        """Load cleaned datasets from Google Drive URLs and concatenate them with a Country column.
        
        Returns:
            pd.DataFrame: Combined DataFrame with 'Country' and 'Timestamp' columns.
        
        Raises:
            Exception: If data loading fails due to URL issues or file errors.
        """
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

            self.data = pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)
            self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'])
            return self.data
        except Exception as e:
            raise Exception(f"Failed to load data: {str(e)}")

    def get_top_regions(self, metric='GHI', top_n=3):
        """Get top regions by average metric (e.g., GHI).
        
        Args:
            metric (str): Column name to rank by (default: 'GHI').
            top_n (int): Number of top regions to return (default: 3).
        
        Returns:
            pd.DataFrame: DataFrame with top regions and their average metric.
        
        Raises:
            KeyError: If the metric column is not found in the DataFrame.
        """
        try:
            avg_metric = self.data.groupby('Country')[metric].mean().sort_values(ascending=False)
            return avg_metric.head(top_n).reset_index()
        except KeyError as e:
            raise KeyError(f"Metric {metric} not found in DataFrame: {str(e)}")