def to_latex(self, buf: Optional[FilePathOrBuffer[str]]=None, column_format: Optional[str]=None, longtable: bool=False, encoding: Optional[str]=None, multicolumn: bool=False, multicolumn_format: Optional[str]=None, multirow: bool=False, caption: Optional[str]=None, label: Optional[str]=None) -> Optional[str]:
    """
        Render a DataFrame to a LaTeX tabular/longtable environment output.
        """
    from pandas.io.formats.latex import LatexFormatter
    return LatexFormatter(self, column_format=column_format, longtable=longtable, multicolumn=multicolumn, multicolumn_format=multicolumn_format, multirow=multirow, caption=caption, label=label).get_result(buf=buf, encoding=encoding)