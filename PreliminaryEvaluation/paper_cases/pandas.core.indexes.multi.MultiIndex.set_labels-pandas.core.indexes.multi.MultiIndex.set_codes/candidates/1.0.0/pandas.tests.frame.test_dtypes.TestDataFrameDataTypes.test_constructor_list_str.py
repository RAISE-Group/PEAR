@pytest.mark.parametrize('input_vals', [[1, 2], ['1', '2'], list(pd.date_range('1/1/2011', periods=2, freq='H')), list(pd.date_range('1/1/2011', periods=2, freq='H', tz='US/Eastern')), [pd.Interval(left=0, right=5)]])
def test_constructor_list_str(self, input_vals, string_dtype):
    result = DataFrame({'A': input_vals}, dtype=string_dtype)
    expected = DataFrame({'A': input_vals}).astype({'A': string_dtype})
    tm.assert_frame_equal(result, expected)