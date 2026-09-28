def test_maybe_numeric_slice(self):
    df = DataFrame({'A': [1, 2], 'B': ['c', 'd'], 'C': [True, False]})
    result = _maybe_numeric_slice(df, slice_=None)
    expected = pd.IndexSlice[:, ['A']]
    assert result == expected
    result = _maybe_numeric_slice(df, None, include_bool=True)
    expected = pd.IndexSlice[:, ['A', 'C']]
    result = _maybe_numeric_slice(df, [1])
    expected = [1]
    assert result == expected