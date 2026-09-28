@pytest.mark.parametrize('func', ['maximum', 'minimum'])
def test_numpy_reduction_with_tz_aware_dtype(self, tz_aware_fixture, func):
    tz = tz_aware_fixture
    arg = pd.to_datetime(['2019']).tz_localize(tz)
    expected = Series(arg)
    result = getattr(np, func)(expected, expected)
    tm.assert_series_equal(result, expected)