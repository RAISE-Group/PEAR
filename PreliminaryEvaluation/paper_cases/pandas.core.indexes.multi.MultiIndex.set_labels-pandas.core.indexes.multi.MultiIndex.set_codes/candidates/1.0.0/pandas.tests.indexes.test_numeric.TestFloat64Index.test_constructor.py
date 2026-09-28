def test_constructor(self):
    index = Float64Index([1, 2, 3, 4, 5])
    assert isinstance(index, Float64Index)
    expected = np.array([1, 2, 3, 4, 5], dtype='float64')
    tm.assert_numpy_array_equal(index.values, expected)
    index = Float64Index(np.array([1, 2, 3, 4, 5]))
    assert isinstance(index, Float64Index)
    index = Float64Index([1.0, 2, 3, 4, 5])
    assert isinstance(index, Float64Index)
    index = Float64Index(np.array([1.0, 2, 3, 4, 5]))
    assert isinstance(index, Float64Index)
    assert index.dtype == float
    index = Float64Index(np.array([1.0, 2, 3, 4, 5]), dtype=np.float32)
    assert isinstance(index, Float64Index)
    assert index.dtype == np.float64
    index = Float64Index(np.array([1, 2, 3, 4, 5]), dtype=np.float32)
    assert isinstance(index, Float64Index)
    assert index.dtype == np.float64
    result = Float64Index([np.nan, np.nan])
    assert pd.isna(result.values).all()
    result = Float64Index(np.array([np.nan]))
    assert pd.isna(result.values).all()
    result = Index(np.array([np.nan]))
    assert pd.isna(result.values).all()