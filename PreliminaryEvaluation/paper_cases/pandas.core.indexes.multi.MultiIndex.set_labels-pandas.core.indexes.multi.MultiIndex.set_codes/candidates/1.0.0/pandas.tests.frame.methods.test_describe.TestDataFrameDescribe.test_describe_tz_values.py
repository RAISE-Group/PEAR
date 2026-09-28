def test_describe_tz_values(self, tz_naive_fixture):
    tz = tz_naive_fixture
    s1 = Series(range(5))
    start = Timestamp(2018, 1, 1)
    end = Timestamp(2018, 1, 5)
    s2 = Series(date_range(start, end, tz=tz))
    df = pd.DataFrame({'s1': s1, 's2': s2})
    expected = DataFrame({'s1': [5, np.nan, np.nan, np.nan, np.nan, np.nan, 2, 1.581139, 0, 1, 2, 3, 4], 's2': [5, 5, s2.value_counts().index[0], 1, start.tz_localize(tz), end.tz_localize(tz), np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]}, index=['count', 'unique', 'top', 'freq', 'first', 'last', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
    result = df.describe(include='all')
    tm.assert_frame_equal(result, expected)