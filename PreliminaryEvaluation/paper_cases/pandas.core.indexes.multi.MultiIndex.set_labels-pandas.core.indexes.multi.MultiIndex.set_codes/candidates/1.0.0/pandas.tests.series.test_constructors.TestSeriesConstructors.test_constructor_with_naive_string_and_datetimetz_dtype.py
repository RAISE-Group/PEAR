@pytest.mark.parametrize('arg', ['2013-01-01 00:00:00', pd.NaT, np.nan, None])
def test_constructor_with_naive_string_and_datetimetz_dtype(self, arg):
    result = Series([arg], dtype='datetime64[ns, CET]')
    expected = Series(pd.Timestamp(arg)).dt.tz_localize('CET')
    tm.assert_series_equal(result, expected)