@pytest.mark.parametrize('val', [datetime(2000, 1, 4), datetime(2000, 1, 5)])
def test_series_comparison_scalars(self, val):
    series = Series(date_range('1/1/2000', periods=10))
    result = series > val
    expected = Series([x > val for x in series])
    tm.assert_series_equal(result, expected)