def test_merge_all_na_column(self, series_of_dtype, series_of_dtype_all_na):
    df_left = pd.DataFrame({'key': series_of_dtype, 'value': series_of_dtype_all_na}, columns=['key', 'value'])
    df_right = pd.DataFrame({'key': series_of_dtype, 'value': series_of_dtype_all_na}, columns=['key', 'value'])
    expected = pd.DataFrame({'key': series_of_dtype, 'value_x': series_of_dtype_all_na, 'value_y': series_of_dtype_all_na}, columns=['key', 'value_x', 'value_y'])
    actual = df_left.merge(df_right, on='key')
    tm.assert_frame_equal(actual, expected)