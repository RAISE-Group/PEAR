def to_sql(self, frame, name, if_exists='fail', index=True, index_label=None, schema=None, chunksize=None, dtype=None, method=None):
    """
        Write records stored in a DataFrame to a SQL database.

        Parameters
        ----------
        frame : DataFrame
        name : string
            Name of SQL table.
        if_exists : {'fail', 'replace', 'append'}, default 'fail'
            - fail: If table exists, do nothing.
            - replace: If table exists, drop it, recreate it, and insert data.
            - append: If table exists, insert data. Create if does not exist.
        index : boolean, default True
            Write DataFrame index as a column.
        index_label : string or sequence, default None
            Column label for index column(s). If None is given (default) and
            `index` is True, then the index names are used.
            A sequence should be given if the DataFrame uses MultiIndex.
        schema : string, default None
            Name of SQL schema in database to write to (if database flavor
            supports this). If specified, this overwrites the default
            schema of the SQLDatabase object.
        chunksize : int, default None
            If not None, then rows will be written in batches of this size at a
            time.  If None, all rows will be written at once.
        dtype : single type or dict of column name to SQL type, default None
            Optional specifying the datatype for columns. The SQL type should
            be a SQLAlchemy type. If all columns are of the same type, one
            single value can be used.
        method : {None', 'multi', callable}, default None
            Controls the SQL insertion clause used:

            * None : Uses standard SQL ``INSERT`` clause (one per row).
            * 'multi': Pass multiple values in a single ``INSERT`` clause.
            * callable with signature ``(pd_table, conn, keys, data_iter)``.

            Details and a sample callable implementation can be found in the
            section :ref:`insert method <io.sql.method>`.

            .. versionadded:: 0.24.0
        """
    if dtype and (not is_dict_like(dtype)):
        dtype = {col_name: dtype for col_name in frame}
    if dtype is not None:
        from sqlalchemy.types import to_instance, TypeEngine
        for col, my_type in dtype.items():
            if not isinstance(to_instance(my_type), TypeEngine):
                raise ValueError(f'The type of {col} is not a SQLAlchemy type')
    table = SQLTable(name, self, frame=frame, index=index, if_exists=if_exists, index_label=index_label, schema=schema, dtype=dtype)
    table.create()
    table.insert(chunksize, method=method)
    if not name.isdigit() and (not name.islower()):
        engine = self.connectable.engine
        with self.connectable.connect() as conn:
            table_names = engine.table_names(schema=schema or self.meta.schema, connection=conn)
        if name not in table_names:
            msg = f"The provided table name '{name}' is not found exactly as such in the database after writing the table, possibly due to case sensitivity issues. Consider using lower case table names."
            warnings.warn(msg, UserWarning)