def test_operators_corner(self, datetime_series):
    empty = Series([], index=Index([]), dtype=np.float64)
    result = datetime_series + empty
    assert np.isnan(result).all()
    result = empty + empty.copy()
    assert len(result) == 0
    int_ts = datetime_series.astype(int)[:-5]
    added = datetime_series + int_ts
    expected = Series(datetime_series.values[:-5] + int_ts.values, index=datetime_series.index[:-5], name='ts')
    tm.assert_series_equal(added[:-5], expected)