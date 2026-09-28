@pytest.mark.parametrize('input,output,diff', [([False, True, True, False, False], [np.nan, True, False, True, False], 1)])
def test_diff_bool(self, input, output, diff):
    s = Series(input)
    result = s.diff()
    expected = Series(output)
    tm.assert_series_equal(result, expected)