def parse(self, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=False, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=True, mangle_dupe_cols=True, **kwds):
    """
        Parse specified sheet(s) into a DataFrame.

        Equivalent to read_excel(ExcelFile, ...)  See the read_excel
        docstring for more info on accepted parameters.

        Returns
        -------
        DataFrame or dict of DataFrames
            DataFrame from the passed in Excel file.
        """
    if 'chunksize' in kwds:
        raise NotImplementedError('chunksize keyword of read_excel is not implemented')
    return self._reader.parse(sheet_name=sheet_name, header=header, names=names, index_col=index_col, usecols=usecols, squeeze=squeeze, converters=converters, true_values=true_values, false_values=false_values, skiprows=skiprows, nrows=nrows, na_values=na_values, parse_dates=parse_dates, date_parser=date_parser, thousands=thousands, comment=comment, skipfooter=skipfooter, convert_float=convert_float, mangle_dupe_cols=mangle_dupe_cols, **kwds)