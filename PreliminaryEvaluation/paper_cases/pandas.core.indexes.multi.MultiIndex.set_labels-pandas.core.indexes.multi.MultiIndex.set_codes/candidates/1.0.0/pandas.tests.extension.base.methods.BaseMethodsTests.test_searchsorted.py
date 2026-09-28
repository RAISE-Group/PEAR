def test_searchsorted(self, data_for_sorting, as_series):
    b, c, a = data_for_sorting
    arr = type(data_for_sorting)._from_sequence([a, b, c])
    if as_series:
        arr = pd.Series(arr)
    assert arr.searchsorted(a) == 0
    assert arr.searchsorted(a, side='right') == 1
    assert arr.searchsorted(b) == 1
    assert arr.searchsorted(b, side='right') == 2
    assert arr.searchsorted(c) == 2
    assert arr.searchsorted(c, side='right') == 3
    result = arr.searchsorted(arr.take([0, 2]))
    expected = np.array([0, 2], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)
    sorter = np.array([1, 2, 0])
    assert data_for_sorting.searchsorted(a, sorter=sorter) == 0