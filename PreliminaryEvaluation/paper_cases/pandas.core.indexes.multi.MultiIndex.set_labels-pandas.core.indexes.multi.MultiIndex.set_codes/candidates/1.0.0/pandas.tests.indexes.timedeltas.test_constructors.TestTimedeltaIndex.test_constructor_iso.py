def test_constructor_iso(self):
    expected = timedelta_range('1s', periods=9, freq='s')
    durations = ['P0DT0H0M{}S'.format(i) for i in range(1, 10)]
    result = to_timedelta(durations)
    tm.assert_index_equal(result, expected)