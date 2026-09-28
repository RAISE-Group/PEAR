def test_merge_on_periods(self):
    left = pd.DataFrame({'key': pd.period_range('20151010', periods=2, freq='D'), 'value': [1, 2]})
    right = pd.DataFrame({'key': pd.period_range('20151011', periods=3, freq='D'), 'value': [1, 2, 3]})
    expected = DataFrame({'key': pd.period_range('20151010', periods=4, freq='D'), 'value_x': [1, 2, np.nan, np.nan], 'value_y': [np.nan, 1, 2, 3]})
    result = pd.merge(left, right, on='key', how='outer')
    tm.assert_frame_equal(result, expected)
    left = pd.DataFrame({'key': [1, 2], 'value': pd.period_range('20151010', periods=2, freq='D')})
    right = pd.DataFrame({'key': [2, 3], 'value': pd.period_range('20151011', periods=2, freq='D')})
    exp_x = pd.period_range('20151010', periods=2, freq='D')
    exp_y = pd.period_range('20151011', periods=2, freq='D')
    expected = DataFrame({'key': [1, 2, 3], 'value_x': list(exp_x) + [pd.NaT], 'value_y': [pd.NaT] + list(exp_y)})
    result = pd.merge(left, right, on='key', how='outer')
    tm.assert_frame_equal(result, expected)
    assert result['value_x'].dtype == 'Period[D]'
    assert result['value_y'].dtype == 'Period[D]'