def test_nulls(self, indices):
    if len(indices) == 0:
        tm.assert_numpy_array_equal(indices.isna(), np.array([], dtype=bool))
    elif isinstance(indices, MultiIndex):
        idx = indices.copy()
        msg = 'isna is not defined for MultiIndex'
        with pytest.raises(NotImplementedError, match=msg):
            idx.isna()
    elif not indices.hasnans:
        tm.assert_numpy_array_equal(indices.isna(), np.zeros(len(indices), dtype=bool))
        tm.assert_numpy_array_equal(indices.notna(), np.ones(len(indices), dtype=bool))
    else:
        result = isna(indices)
        tm.assert_numpy_array_equal(indices.isna(), result)
        tm.assert_numpy_array_equal(indices.notna(), ~result)