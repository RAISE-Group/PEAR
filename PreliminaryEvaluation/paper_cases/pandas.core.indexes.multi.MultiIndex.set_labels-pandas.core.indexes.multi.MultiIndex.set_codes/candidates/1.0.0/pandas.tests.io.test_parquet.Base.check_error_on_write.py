def check_error_on_write(self, df, engine, exc):
    with tm.ensure_clean() as path:
        with pytest.raises(exc):
            to_parquet(df, path, engine, compression=None)