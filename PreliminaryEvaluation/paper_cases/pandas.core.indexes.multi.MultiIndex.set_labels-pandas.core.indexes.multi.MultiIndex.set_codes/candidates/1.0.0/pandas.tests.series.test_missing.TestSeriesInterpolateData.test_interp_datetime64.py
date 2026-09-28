@td.skip_if_no_scipy
@pytest.mark.parametrize('method', ['nearest', 'pad'])
def test_interp_datetime64(self, method, tz_naive_fixture):
    df = Series([1, np.nan, 3], index=date_range('1/1/2000', periods=3, tz=tz_naive_fixture))
    result = df.interpolate(method=method)
    expected = Series([1.0, 1.0, 3.0], index=date_range('1/1/2000', periods=3, tz=tz_naive_fixture))
    tm.assert_series_equal(result, expected)