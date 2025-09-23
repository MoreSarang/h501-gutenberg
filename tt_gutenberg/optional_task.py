import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_avg_languages_by_birth_century(df: pd.DataFrame):
    """
    Create a Seaborn barplot showing average number of languages associated with authors born in each century.
    """
    df = df.copy()
    
    # Convert birthdate to birth century (floor division by 100 and multiply by 100)
    df['birth_century'] = (np.floor(df['birthdate'] / 100) * 100).astype('Int64')
    
    # Count number of languages, assuming each row corresponds to one language translation (approximation)
    # Group by author and birth_century to get the number of languages per author
    author_lang_counts = (
        df.groupby(['author', 'birth_century'])
        .agg(lang_count=('alias', 'nunique'))  # Using alias count as proxy for languages
        .reset_index()
    )
    
    # Group by birth_century and calculate the average languages per author
    century_avg = author_lang_counts.groupby('birth_century').agg(avg_lang=('lang_count', 'mean')).reset_index()
    
    # Plot with 95% confidence interval
    plt.figure(figsize=(10, 6))
    sns.barplot(data=century_avg, x='birth_century', y='avg_lang', ci=95)
    plt.xlabel('Birth Century')
    plt.ylabel('Average Number of Languages')
    plt.title('Average Number of Languages per Author by Birth Century')
    plt.show()
