from .utils import get_author_aliases


def list_authors(by_languages=False, alias=False, df=None):
    """
    If alias=True and df is provided, returns list of author aliases
    sorted by translation count.
    """
    if alias and df is not None:
        return get_author_aliases(df)
    return []
