@pytest.mark.parametrize('arr, val', [[pd.date_range('20120101', periods=10, freq='2D'), pd.Timestamp('20120102')], [pd.date_range('20120101', periods=10, freq='2D', tz='Asia/Hong_Kong'), pd.Timestamp('20120102', tz='Asia/Hong_Kong')], [pd.timedelta_range(start='1 day', end='10 days', periods=10), pd.Timedelta('2 days')]])
def test_search_sorted_datetime64_scalar(self, arr, val):
    arr = pd.array(arr)
    result = arr.searchsorted(val)
    assert is_scalar(result)
    assert result == 1