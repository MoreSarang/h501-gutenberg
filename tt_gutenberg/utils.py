import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def get_author_aliases(df: pd.DataFrame) -> list:
    """
    Given a dataframe of Gutenberg authors, return a list of author aliases
    sorted by translation count in descending order.

    Messy or NaN alias values are excluded.
    """
    # Filter rows where alias is not null or NaN
    df_clean = df[df['alias'].notna()]

    # Group by alias and count entries
    counts = df_clean.groupby('alias').size().sort_values(ascending=False)

    # Return list of aliases sorted by count descending
    return counts.index.to_list()

def plot_translations(df: pd.DataFrame, over='birth_century'):
    """
    Plots a Seaborn barplot showing average number of author translations by birth century.
    
    Parameters:
        df - DataFrame containing Gutenberg authors data.
        over - str, the grouping column; should be 'birth_century'.
    """
    df = df.copy()
    
    # Create birth_century column by flooring birthdate to century
    df['birth_century'] = (np.floor(df['birthdate'] / 100) * 100).astype('Int64')
    
    # Group by author and birth_century, counting unique aliases as translation proxy
    author_alias_counts = (
        df.groupby(['author', 'birth_century'])
        .agg(translation_count=('alias', 'nunique'))
        .reset_index()
    )
    
    # Calculate average translations per birth century
    centroid_data = author_alias_counts.groupby('birth_century').agg(
        avg_translations=('translation_count', 'mean')
    ).reset_index()
    
    # Plot with seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(data=centroid_data, x='birth_century', y='avg_translations', ci=95)
    plt.xlabel('Birth Century')
    plt.ylabel('Average Number of Translations')
    plt.title('Average Author Translation Count by Birth Century')
    plt.show()
