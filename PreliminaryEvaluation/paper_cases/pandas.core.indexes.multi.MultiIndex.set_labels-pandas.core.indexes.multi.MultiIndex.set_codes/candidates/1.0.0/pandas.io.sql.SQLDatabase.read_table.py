def read_table(self, table_name, index_col=None, coerce_float=True, parse_dates=None, columns=None, schema=None, chunksize=None):
    """Read SQL database table into a DataFrame.

        Parameters
        ----------
        table_name : string
            Name of SQL table in database.
        index_col : string, optional, default: None
            Column to set as index.
        coerce_float : boolean, default True
            Attempts to convert values of non-string, non-numeric objects
            (like decimal.Decimal) to floating point. This can result in
            loss of precision.
        parse_dates : list or dict, default: None
            - List of column names to parse as dates.
            - Dict of ``{column_name: format string}`` where format string is
              strftime compatible in case of parsing string times, or is one of
              (D, s, ns, ms, us) in case of parsing integer timestamps.
            - Dict of ``{column_name: arg}``, where the arg corresponds
              to the keyword arguments of :func:`pandas.to_datetime`.
              Especially useful with databases without native Datetime support,
              such as SQLite.
        columns : list, default: None
            List of column names to select from SQL table.
        schema : string, default None
            Name of SQL schema in database to query (if database flavor
            supports this).  If specified, this overwrites the default
            schema of the SQL database object.
        chunksize : int, default None
            If specified, return an iterator where `chunksize` is the number
            of rows to include in each chunk.

        Returns
        -------
        DataFrame

        See Also
        --------
        pandas.read_sql_table
        SQLDatabase.read_query

        """
    table = SQLTable(table_name, self, index=index_col, schema=schema)
    return table.read(coerce_float=coerce_float, parse_dates=parse_dates, columns=columns, chunksize=chunksize)