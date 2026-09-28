def test_long_strings(self, setup_path):
    df = DataFrame({'a': tm.rands_array(100, size=10)}, index=tm.rands_array(100, size=10))
    with ensure_clean_store(setup_path) as store:
        store.append('df', df, data_columns=['a'])
        result = store.select('df')
        tm.assert_frame_equal(df, result)