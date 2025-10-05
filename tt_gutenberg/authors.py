# authors.py
from .utils import get_author_aliases, plot_translations


def list_authors(by_languages=False, alias=False, authors=None, languages=None, metadata=None):

    # If alias requested and all datasets provided, calculate translation counts by alias using languages and metadata
    if alias and authors is not None and languages is not None and metadata is not None:
        # Merge metadata and languages to link books with language info
        meta_lang = metadata.merge(languages, on='gutenberg_id', how='left')
        # Merge with authors to map author aliases to books
        merged = meta_lang.merge(authors, left_on='gutenberg_author_id', right_on='gutenberg_author_id', how='left')
        # Remove entries missing alias or language info
        merged = merged[merged['alias'].notna() & merged['language'].notna()]
        # Group aliases by unique languages count and sort descending
        alias_lang_counts = merged.groupby('alias')['language'].nunique().sort_values(ascending=False)
        return alias_lang_counts.index.to_list()
    # Fall-back: if only authors dataset and alias requested
    elif alias and authors is not None:
        return get_author_aliases(authors)
    else:
        return []

def plot_translations_over_century(df=None):
    if df is not None:
        plot_translations(df)
