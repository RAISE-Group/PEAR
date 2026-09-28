def test_fillna(self, indices):
    if len(indices) == 0:
        pass
    elif isinstance(indices, MultiIndex):
        idx = indices.copy(deep=True)
        msg = 'isna is not defined for MultiIndex'
        with pytest.raises(NotImplementedError, match=msg):
            idx.fillna(idx[0])
    else:
        idx = indices.copy(deep=True)
        result = idx.fillna(idx[0])
        tm.assert_index_equal(result, idx)
        assert result is not idx
        msg = "'value' must be a scalar, passed: "
        with pytest.raises(TypeError, match=msg):
            idx.fillna([idx[0]])
        idx = indices.copy(deep=True)
        values = np.asarray(idx.values)
        if isinstance(indices, DatetimeIndexOpsMixin):
            values[1] = iNaT
        elif isinstance(indices, (Int64Index, UInt64Index)):
            return
        else:
            values[1] = np.nan
        if isinstance(indices, PeriodIndex):
            idx = type(indices)(values, freq=indices.freq)
        else:
            idx = type(indices)(values)
        expected = np.array([False] * len(idx), dtype=bool)
        expected[1] = True
        tm.assert_numpy_array_equal(idx._isnan, expected)
        assert idx.hasnans is True