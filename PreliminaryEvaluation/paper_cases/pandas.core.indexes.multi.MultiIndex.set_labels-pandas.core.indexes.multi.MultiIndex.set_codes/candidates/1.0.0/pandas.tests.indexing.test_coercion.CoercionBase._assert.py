def _assert(self, left, right, dtype):
    if isinstance(left, pd.Series):
        tm.assert_series_equal(left, right)
    elif isinstance(left, pd.Index):
        tm.assert_index_equal(left, right)
    else:
        raise NotImplementedError
    assert left.dtype == dtype
    assert right.dtype == dtype