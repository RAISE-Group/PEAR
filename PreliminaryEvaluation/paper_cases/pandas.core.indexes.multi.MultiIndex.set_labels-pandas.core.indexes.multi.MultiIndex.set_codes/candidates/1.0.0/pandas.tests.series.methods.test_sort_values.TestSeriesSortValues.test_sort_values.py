def test_sort_values(self, datetime_series):
    ser = Series([3, 2, 4, 1], ['A', 'B', 'C', 'D'])
    expected = Series([1, 2, 3, 4], ['D', 'B', 'A', 'C'])
    result = ser.sort_values()
    tm.assert_series_equal(expected, result)
    ts = datetime_series.copy()
    ts[:5] = np.NaN
    vals = ts.values
    result = ts.sort_values()
    assert np.isnan(result[-5:]).all()
    tm.assert_numpy_array_equal(result[:-5].values, np.sort(vals[5:]))
    result = ts.sort_values(na_position='first')
    assert np.isnan(result[:5]).all()
    tm.assert_numpy_array_equal(result[5:].values, np.sort(vals[5:]))
    ser = Series(['A', 'B'], [1, 2])
    ser.sort_values()
    ordered = ts.sort_values(ascending=False)
    expected = np.sort(ts.dropna().values)[::-1]
    tm.assert_almost_equal(expected, ordered.dropna().values)
    ordered = ts.sort_values(ascending=False, na_position='first')
    tm.assert_almost_equal(expected, ordered.dropna().values)
    ordered = ts.sort_values(ascending=[False])
    expected = ts.sort_values(ascending=False)
    tm.assert_series_equal(expected, ordered)
    ordered = ts.sort_values(ascending=[False], na_position='first')
    expected = ts.sort_values(ascending=False, na_position='first')
    tm.assert_series_equal(expected, ordered)
    msg = 'ascending must be boolean'
    with pytest.raises(ValueError, match=msg):
        ts.sort_values(ascending=None)
    msg = 'Length of ascending \\(0\\) must be 1 for Series'
    with pytest.raises(ValueError, match=msg):
        ts.sort_values(ascending=[])
    msg = 'Length of ascending \\(3\\) must be 1 for Series'
    with pytest.raises(ValueError, match=msg):
        ts.sort_values(ascending=[1, 2, 3])
    msg = 'Length of ascending \\(2\\) must be 1 for Series'
    with pytest.raises(ValueError, match=msg):
        ts.sort_values(ascending=[False, False])
    msg = 'ascending must be boolean'
    with pytest.raises(ValueError, match=msg):
        ts.sort_values(ascending='foobar')
    ts = datetime_series.copy()
    ts.sort_values(ascending=False, inplace=True)
    tm.assert_series_equal(ts, datetime_series.sort_values(ascending=False))
    tm.assert_index_equal(ts.index, datetime_series.sort_values(ascending=False).index)
    df = DataFrame(np.random.randn(10, 4))
    s = df.iloc[:, 0]
    msg = 'This Series is a view of some other array, to sort in-place you must create a copy'
    with pytest.raises(ValueError, match=msg):
        s.sort_values(inplace=True)