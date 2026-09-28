def test_merge_on_datetime64tz_empty(self):
    dtz = pd.DatetimeTZDtype(tz='UTC')
    right = pd.DataFrame({'date': [pd.Timestamp('2018', tz=dtz.tz)], 'value': [4.0], 'date2': [pd.Timestamp('2019', tz=dtz.tz)]}, columns=['date', 'value', 'date2'])
    left = right[:0]
    result = left.merge(right, on='date')
    expected = pd.DataFrame({'value_x': pd.Series(dtype=float), 'date2_x': pd.Series(dtype=dtz), 'date': pd.Series(dtype=dtz), 'value_y': pd.Series(dtype=float), 'date2_y': pd.Series(dtype=dtz)}, columns=['value_x', 'date2_x', 'date', 'value_y', 'date2_y'])
    tm.assert_frame_equal(result, expected)