def test_swapcase(self):
    values = Series(['FOO', 'BAR', np.nan, 'Blah', 'blurg'])
    result = values.str.swapcase()
    exp = Series(['foo', 'bar', np.nan, 'bLAH', 'BLURG'])
    tm.assert_series_equal(result, exp)
    mixed = Series(['FOO', np.nan, 'bar', True, datetime.today(), 'Blah', None, 1, 2.0])
    mixed = mixed.str.swapcase()
    exp = Series(['foo', np.nan, 'BAR', np.nan, np.nan, 'bLAH', np.nan, np.nan, np.nan])
    tm.assert_almost_equal(mixed, exp)