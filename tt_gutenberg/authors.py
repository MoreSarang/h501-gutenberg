from .utils import get_author_aliases


def list_authors(by_languages=False, alias=False, df=None):
    """
    If alias=True and df is provided, returns list of author aliases
    sorted by translation count.

    Supports placeholder for by_languages flag.
    """
    if alias and df is not None:
        return get_author_aliases(df)
    
    # You can add support for by_languages or other cases as needed
    return []
