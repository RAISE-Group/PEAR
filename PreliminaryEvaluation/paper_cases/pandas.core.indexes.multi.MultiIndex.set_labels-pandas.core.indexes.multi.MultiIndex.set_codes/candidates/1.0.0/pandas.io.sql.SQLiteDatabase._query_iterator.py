@staticmethod
def _query_iterator(cursor, chunksize, columns, index_col=None, coerce_float=True, parse_dates=None):
    """Return generator through chunked result set"""
    while True:
        data = cursor.fetchmany(chunksize)
        if type(data) == tuple:
            data = list(data)
        if not data:
            cursor.close()
            break
        else:
            yield _wrap_result(data, columns, index_col=index_col, coerce_float=coerce_float, parse_dates=parse_dates)