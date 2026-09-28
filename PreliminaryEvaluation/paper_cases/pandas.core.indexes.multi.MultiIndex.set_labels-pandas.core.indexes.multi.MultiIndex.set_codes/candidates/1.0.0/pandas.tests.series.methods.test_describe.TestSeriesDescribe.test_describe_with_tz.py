def test_describe_with_tz(self, tz_naive_fixture):
    tz = tz_naive_fixture
    name = str(tz_naive_fixture)
    start = Timestamp(2018, 1, 1)
    end = Timestamp(2018, 1, 5)
    s = Series(date_range(start, end, tz=tz), name=name)
    result = s.describe()
    expected = Series([5, 5, s.value_counts().index[0], 1, start.tz_localize(tz), end.tz_localize(tz)], name=name, index=['count', 'unique', 'top', 'freq', 'first', 'last'])
    tm.assert_series_equal(result, expected)