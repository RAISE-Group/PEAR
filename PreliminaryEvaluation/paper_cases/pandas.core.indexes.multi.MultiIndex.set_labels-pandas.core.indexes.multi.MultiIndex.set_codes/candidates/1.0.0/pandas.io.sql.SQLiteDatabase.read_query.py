def read_query(self, sql, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None):
    args = _convert_params(sql, params)
    cursor = self.execute(*args)
    columns = [col_desc[0] for col_desc in cursor.description]
    if chunksize is not None:
        return self._query_iterator(cursor, chunksize, columns, index_col=index_col, coerce_float=coerce_float, parse_dates=parse_dates)
    else:
        data = self._fetchall_as_list(cursor)
        cursor.close()
        frame = _wrap_result(data, columns, index_col=index_col, coerce_float=coerce_float, parse_dates=parse_dates)
        return frame