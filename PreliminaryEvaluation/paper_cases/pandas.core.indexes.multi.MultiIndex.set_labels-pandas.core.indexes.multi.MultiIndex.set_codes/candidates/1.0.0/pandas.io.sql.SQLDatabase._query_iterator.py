@staticmethod
def _query_iterator(result, chunksize, columns, index_col=None, coerce_float=True, parse_dates=None):
    """Return generator through chunked result set"""
    while True:
        data = result.fetchmany(chunksize)
        if not data:
            break
        else:
            yield _wrap_result(data, columns, index_col=index_col, coerce_float=coerce_float, parse_dates=parse_dates)