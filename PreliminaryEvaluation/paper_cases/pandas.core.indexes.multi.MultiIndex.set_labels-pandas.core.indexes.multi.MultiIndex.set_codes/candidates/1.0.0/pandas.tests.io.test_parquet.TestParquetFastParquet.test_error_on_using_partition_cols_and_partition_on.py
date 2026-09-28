def test_error_on_using_partition_cols_and_partition_on(self, fp, df_full):
    partition_cols = ['bool', 'int']
    df = df_full
    with pytest.raises(ValueError):
        with tm.ensure_clean_dir() as path:
            df.to_parquet(path, engine='fastparquet', compression=None, partition_on=partition_cols, partition_cols=partition_cols)