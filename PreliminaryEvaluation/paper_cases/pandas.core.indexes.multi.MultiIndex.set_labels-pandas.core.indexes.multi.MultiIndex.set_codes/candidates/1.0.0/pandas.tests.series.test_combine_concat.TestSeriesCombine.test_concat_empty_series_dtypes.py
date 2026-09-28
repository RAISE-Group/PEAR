def test_concat_empty_series_dtypes(self):
    assert pd.concat([Series(dtype=np.bool_), Series(dtype=np.int32)]).dtype == np.int32
    assert pd.concat([Series(dtype=np.bool_), Series(dtype=np.float32)]).dtype == np.object_
    assert pd.concat([Series(dtype='m8[ns]'), Series(dtype=np.bool)]).dtype == np.object_
    assert pd.concat([Series(dtype='m8[ns]'), Series(dtype=np.int64)]).dtype == np.object_
    assert pd.concat([Series(dtype='M8[ns]'), Series(dtype=np.bool)]).dtype == np.object_
    assert pd.concat([Series(dtype='M8[ns]'), Series(dtype=np.int64)]).dtype == np.object_
    assert pd.concat([Series(dtype='M8[ns]'), Series(dtype=np.bool_), Series(dtype=np.int64)]).dtype == np.object_
    assert pd.concat([Series(dtype='category'), Series(dtype='category')]).dtype == 'category'
    assert pd.concat([Series(np.array([]), dtype='category'), Series(dtype='float64')]).dtype == 'float64'
    assert pd.concat([Series(dtype='category'), Series(dtype='object')]).dtype == 'object'
    result = pd.concat([Series(dtype='float64').astype('Sparse'), Series(dtype='float64').astype('Sparse')])
    assert result.dtype == 'Sparse[float64]'
    result = pd.concat([Series(dtype='float64').astype('Sparse'), Series(dtype='float64')])
    expected = pd.SparseDtype(np.float64)
    assert result.dtype == expected
    result = pd.concat([Series(dtype='float64').astype('Sparse'), Series(dtype='object')])
    expected = pd.SparseDtype('object')
    assert result.dtype == expected