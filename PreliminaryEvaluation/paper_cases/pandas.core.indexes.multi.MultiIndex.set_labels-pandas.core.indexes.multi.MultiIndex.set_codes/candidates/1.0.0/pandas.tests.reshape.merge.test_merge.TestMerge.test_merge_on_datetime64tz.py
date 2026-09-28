def test_merge_on_datetime64tz(self):
    left = pd.DataFrame({'key': pd.date_range('20151010', periods=2, tz='US/Eastern'), 'value': [1, 2]})
    right = pd.DataFrame({'key': pd.date_range('20151011', periods=3, tz='US/Eastern'), 'value': [1, 2, 3]})
    expected = DataFrame({'key': pd.date_range('20151010', periods=4, tz='US/Eastern'), 'value_x': [1, 2, np.nan, np.nan], 'value_y': [np.nan, 1, 2, 3]})
    result = pd.merge(left, right, on='key', how='outer')
    tm.assert_frame_equal(result, expected)
    left = pd.DataFrame({'key': [1, 2], 'value': pd.date_range('20151010', periods=2, tz='US/Eastern')})
    right = pd.DataFrame({'key': [2, 3], 'value': pd.date_range('20151011', periods=2, tz='US/Eastern')})
    expected = DataFrame({'key': [1, 2, 3], 'value_x': list(pd.date_range('20151010', periods=2, tz='US/Eastern')) + [pd.NaT], 'value_y': [pd.NaT] + list(pd.date_range('20151011', periods=2, tz='US/Eastern'))})
    result = pd.merge(left, right, on='key', how='outer')
    tm.assert_frame_equal(result, expected)
    assert result['value_x'].dtype == 'datetime64[ns, US/Eastern]'
    assert result['value_y'].dtype == 'datetime64[ns, US/Eastern]'