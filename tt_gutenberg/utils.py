import pandas as pd


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
