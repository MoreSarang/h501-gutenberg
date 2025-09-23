from .utils import get_author_aliases, plot_translations


def list_authors(by_languages=False, alias=False, df=None):
    if alias and df is not None:
        return get_author_aliases(df)
    return []

def plot_translations_over_century(df=None):
    if df is not None:
        plot_translations(df)
