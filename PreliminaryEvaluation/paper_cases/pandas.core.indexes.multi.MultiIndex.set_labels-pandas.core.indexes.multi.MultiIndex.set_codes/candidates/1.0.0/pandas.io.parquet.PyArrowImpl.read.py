def read(self, path, columns=None, **kwargs):
    path, _, _, should_close = get_filepath_or_buffer(path)
    kwargs['use_pandas_metadata'] = True
    result = self.api.parquet.read_table(path, columns=columns, **kwargs).to_pandas()
    if should_close:
        path.close()
    return result