def test_title(self):
    values = Series(['FOO', 'BAR', np.nan, 'Blah', 'blurg'])
    result = values.str.title()
    exp = Series(['Foo', 'Bar', np.nan, 'Blah', 'Blurg'])
    tm.assert_series_equal(result, exp)
    mixed = Series(['FOO', np.nan, 'bar', True, datetime.today(), 'blah', None, 1, 2.0])
    mixed = mixed.str.title()
    exp = Series(['Foo', np.nan, 'Bar', np.nan, np.nan, 'Blah', np.nan, np.nan, np.nan])
    tm.assert_almost_equal(mixed, exp)