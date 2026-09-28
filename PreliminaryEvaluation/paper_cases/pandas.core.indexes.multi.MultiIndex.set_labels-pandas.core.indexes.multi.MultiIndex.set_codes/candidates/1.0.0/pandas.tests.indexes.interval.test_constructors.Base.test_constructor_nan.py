@pytest.mark.parametrize('breaks', [[np.nan] * 2, [np.nan] * 4, [np.nan] * 50])
def test_constructor_nan(self, constructor, breaks, closed):
    result_kwargs = self.get_kwargs_from_breaks(breaks)
    result = constructor(closed=closed, **result_kwargs)
    expected_subtype = np.float64
    expected_values = np.array(breaks[:-1], dtype=object)
    assert result.closed == closed
    assert result.dtype.subtype == expected_subtype
    tm.assert_numpy_array_equal(result._ndarray_values, expected_values)