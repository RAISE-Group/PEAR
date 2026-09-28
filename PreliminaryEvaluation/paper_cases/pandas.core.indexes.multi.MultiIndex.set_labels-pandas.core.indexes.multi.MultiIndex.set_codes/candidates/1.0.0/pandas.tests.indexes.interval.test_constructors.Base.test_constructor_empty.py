@pytest.mark.parametrize('breaks', [[], np.array([], dtype='int64'), np.array([], dtype='float64'), np.array([], dtype='datetime64[ns]'), np.array([], dtype='timedelta64[ns]')])
def test_constructor_empty(self, constructor, breaks, closed):
    result_kwargs = self.get_kwargs_from_breaks(breaks)
    result = constructor(closed=closed, **result_kwargs)
    expected_values = np.array([], dtype=object)
    expected_subtype = getattr(breaks, 'dtype', np.int64)
    assert result.empty
    assert result.closed == closed
    assert result.dtype.subtype == expected_subtype
    tm.assert_numpy_array_equal(result._ndarray_values, expected_values)