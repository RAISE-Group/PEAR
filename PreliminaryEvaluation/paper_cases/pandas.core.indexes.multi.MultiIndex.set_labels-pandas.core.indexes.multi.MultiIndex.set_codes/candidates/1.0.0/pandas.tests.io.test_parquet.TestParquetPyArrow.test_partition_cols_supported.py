def test_partition_cols_supported(self, pa, df_full):
    partition_cols = ['bool', 'int']
    df = df_full
    with tm.ensure_clean_dir() as path:
        df.to_parquet(path, partition_cols=partition_cols, compression=None)
        import pyarrow.parquet as pq
        dataset = pq.ParquetDataset(path, validate_schema=False)
        assert len(dataset.partitions.partition_names) == 2
        assert dataset.partitions.partition_names == set(partition_cols)