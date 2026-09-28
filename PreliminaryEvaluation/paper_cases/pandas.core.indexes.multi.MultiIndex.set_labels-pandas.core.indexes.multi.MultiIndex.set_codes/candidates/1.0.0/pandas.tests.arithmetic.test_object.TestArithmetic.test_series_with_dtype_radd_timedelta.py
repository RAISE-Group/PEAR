@pytest.mark.parametrize('dtype', [None, object])
def test_series_with_dtype_radd_timedelta(self, dtype):
    ser = pd.Series([pd.Timedelta('1 days'), pd.Timedelta('2 days'), pd.Timedelta('3 days')], dtype=dtype)
    expected = pd.Series([pd.Timedelta('4 days'), pd.Timedelta('5 days'), pd.Timedelta('6 days')])
    result = pd.Timedelta('3 days') + ser
    tm.assert_series_equal(result, expected)
    result = ser + pd.Timedelta('3 days')
    tm.assert_series_equal(result, expected)