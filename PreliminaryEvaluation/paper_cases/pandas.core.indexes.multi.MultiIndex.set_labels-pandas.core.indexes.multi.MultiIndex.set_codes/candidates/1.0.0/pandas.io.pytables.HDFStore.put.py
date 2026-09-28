def put(self, key: str, value: FrameOrSeries, format=None, index=True, append=False, complib=None, complevel: Optional[int]=None, min_itemsize: Optional[Union[int, Dict[str, int]]]=None, nan_rep=None, data_columns: Optional[List[str]]=None, encoding=None, errors: str='strict'):
    """
        Store object in HDFStore.

        Parameters
        ----------
        key : str
        value : {Series, DataFrame}
        format : 'fixed(f)|table(t)', default is 'fixed'
            fixed(f) : Fixed format
                       Fast writing/reading. Not-appendable, nor searchable.
            table(t) : Table format
                       Write as a PyTables Table structure which may perform
                       worse but allow more flexible operations like searching
                       / selecting subsets of the data.
        append   : bool, default False
            This will force Table format, append the input data to the
            existing.
        data_columns : list, default None
            List of columns to create as data columns, or True to
            use all columns. See `here
            <https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#query-via-data-columns>`__.
        encoding : str, default None
            Provide an encoding for strings.
        dropna   : bool, default False, do not write an ALL nan row to
            The store settable by the option 'io.hdf.dropna_table'.
        """
    if format is None:
        format = get_option('io.hdf.default_format') or 'fixed'
    format = self._validate_format(format)
    self._write_to_group(key, value, format=format, index=index, append=append, complib=complib, complevel=complevel, min_itemsize=min_itemsize, nan_rep=nan_rep, data_columns=data_columns, encoding=encoding, errors=errors)