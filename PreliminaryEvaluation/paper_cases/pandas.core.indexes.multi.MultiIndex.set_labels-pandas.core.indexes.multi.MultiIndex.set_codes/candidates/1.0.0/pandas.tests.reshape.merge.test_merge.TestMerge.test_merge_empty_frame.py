def test_merge_empty_frame(self, series_of_dtype, series_of_dtype2):
    df = pd.DataFrame({'key': series_of_dtype, 'value': series_of_dtype2}, columns=['key', 'value'])
    df_empty = df[:0]
    expected = pd.DataFrame({'value_x': pd.Series(dtype=df.dtypes['value']), 'key': pd.Series(dtype=df.dtypes['key']), 'value_y': pd.Series(dtype=df.dtypes['value'])}, columns=['value_x', 'key', 'value_y'])
    actual = df_empty.merge(df, on='key')
    tm.assert_frame_equal(actual, expected)