def test_insert(self):
    idx = RangeIndex(5, name='Foo')
    result = idx[1:4]
    tm.assert_index_equal(idx[0:4], result.insert(0, idx[0]))
    expected = Float64Index([0, np.nan, 1, 2, 3, 4])
    for na in (np.nan, pd.NaT, None):
        result = RangeIndex(5).insert(1, na)
        tm.assert_index_equal(result, expected)