def check_error_on_write(self, df, exc):
    with pytest.raises(exc):
        with tm.ensure_clean() as path:
            to_feather(df, path)