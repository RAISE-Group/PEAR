def test_partition_on_supported(self, fp, df_full):
    partition_cols = ['bool', 'int']
    df = df_full
    with tm.ensure_clean_dir() as path:
        df.to_parquet(path, engine='fastparquet', compression=None, partition_on=partition_cols)
        assert os.path.exists(path)
        import fastparquet
        actual_partition_cols = fastparquet.ParquetFile(path, False).cats
        assert len(actual_partition_cols) == 2