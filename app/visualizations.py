import seaborn as sns
import matplotlib.pyplot as plt

def plot_ghi_distribution(df, countries):
    """Generate a boxplot of GHI distribution for selected countries.
    
    Args:
        df (pd.DataFrame): DataFrame containing solar data.
        countries (list): List of country names to filter.
    
    Returns:
        matplotlib.figure.Figure: Figure object with the plot.
    """
    filtered_df = df[df['Country'].isin(countries)]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Country', y='GHI', data=filtered_df, palette='Set2', ax=ax)
    plt.title('GHI Distribution by Country')
    plt.xlabel('Country')
    plt.ylabel('GHI (W/m²)')
    return fig