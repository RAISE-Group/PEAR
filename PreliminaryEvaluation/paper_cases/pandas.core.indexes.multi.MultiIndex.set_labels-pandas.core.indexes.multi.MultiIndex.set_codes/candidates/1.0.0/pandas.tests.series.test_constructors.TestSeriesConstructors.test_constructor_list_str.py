@pytest.mark.parametrize('input_vals', [[1, 2], ['1', '2'], list(pd.date_range('1/1/2011', periods=2, freq='H')), list(pd.date_range('1/1/2011', periods=2, freq='H', tz='US/Eastern')), [pd.Interval(left=0, right=5)]])
def test_constructor_list_str(self, input_vals, string_dtype):
    result = Series(input_vals, dtype=string_dtype)
    expected = Series(input_vals).astype(string_dtype)
    tm.assert_series_equal(result, expected)