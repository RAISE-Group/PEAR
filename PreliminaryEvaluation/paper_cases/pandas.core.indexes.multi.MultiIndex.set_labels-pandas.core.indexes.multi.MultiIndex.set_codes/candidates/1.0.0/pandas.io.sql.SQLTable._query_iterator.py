def _query_iterator(self, result, chunksize, columns, coerce_float=True, parse_dates=None):
    """Return generator through chunked result set."""
    while True:
        data = result.fetchmany(chunksize)
        if not data:
            break
        else:
            self.frame = DataFrame.from_records(data, columns=columns, coerce_float=coerce_float)
            self._harmonize_columns(parse_dates=parse_dates)
            if self.index is not None:
                self.frame.set_index(self.index, inplace=True)
            yield self.frame