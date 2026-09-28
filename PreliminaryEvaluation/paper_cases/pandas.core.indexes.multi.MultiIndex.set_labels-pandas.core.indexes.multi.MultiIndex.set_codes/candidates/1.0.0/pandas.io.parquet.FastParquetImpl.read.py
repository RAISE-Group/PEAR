def read(self, path, columns=None, **kwargs):
    if is_s3_url(path):
        from pandas.io.s3 import get_file_and_filesystem
        s3, filesystem = get_file_and_filesystem(path)
        try:
            parquet_file = self.api.ParquetFile(path, open_with=filesystem.open)
        finally:
            s3.close()
    else:
        path, _, _, _ = get_filepath_or_buffer(path)
        parquet_file = self.api.ParquetFile(path)
    return parquet_file.to_pandas(columns=columns, **kwargs)