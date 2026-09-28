def test_partition_cols_string(self, fp, df_full):
    partition_cols = 'bool'
    df = df_full
    with tm.ensure_clean_dir() as path:
        df.to_parquet(path, engine='fastparquet', partition_cols=partition_cols, compression=None)
        assert os.path.exists(path)
        import fastparquet
        actual_partition_cols = fastparquet.ParquetFile(path, False).cats
        assert len(actual_partition_cols) == 1