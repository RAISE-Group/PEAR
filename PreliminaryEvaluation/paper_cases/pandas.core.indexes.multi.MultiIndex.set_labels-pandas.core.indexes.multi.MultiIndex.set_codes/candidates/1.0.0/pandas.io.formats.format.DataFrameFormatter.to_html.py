def to_html(self, buf: Optional[FilePathOrBuffer[str]]=None, encoding: Optional[str]=None, classes: Optional[Union[str, List, Tuple]]=None, notebook: bool=False, border: Optional[int]=None) -> Optional[str]:
    """
        Render a DataFrame to a html table.

        Parameters
        ----------
        classes : str or list-like
            classes to include in the `class` attribute of the opening
            ``<table>`` tag, in addition to the default "dataframe".
        notebook : {True, False}, optional, default False
            Whether the generated HTML is for IPython Notebook.
        border : int
            A ``border=border`` attribute is included in the opening
            ``<table>`` tag. Default ``pd.options.display.html.border``.
         """
    from pandas.io.formats.html import HTMLFormatter, NotebookFormatter
    Klass = NotebookFormatter if notebook else HTMLFormatter
    return Klass(self, classes=classes, border=border).get_result(buf=buf, encoding=encoding)