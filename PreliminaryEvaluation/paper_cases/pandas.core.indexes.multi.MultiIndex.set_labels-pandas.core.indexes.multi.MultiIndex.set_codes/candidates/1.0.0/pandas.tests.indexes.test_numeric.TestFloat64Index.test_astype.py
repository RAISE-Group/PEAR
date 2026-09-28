def test_astype(self, mixed_index, float_index):
    result = float_index.astype(object)
    assert result.equals(float_index)
    assert float_index.equals(result)
    self.check_is_index(result)
    i = mixed_index.copy()
    i.name = 'foo'
    result = i.astype(object)
    assert result.equals(i)
    assert i.equals(result)
    self.check_is_index(result)
    for dtype in ['int16', 'int32', 'int64']:
        i = Float64Index([0, 1, 2])
        result = i.astype(dtype)
        expected = Int64Index([0, 1, 2])
        tm.assert_index_equal(result, expected)
        i = Float64Index([0, 1.1, 2])
        result = i.astype(dtype)
        expected = Int64Index([0, 1, 2])
        tm.assert_index_equal(result, expected)
    for dtype in ['float32', 'float64']:
        i = Float64Index([0, 1, 2])
        result = i.astype(dtype)
        expected = i
        tm.assert_index_equal(result, expected)
        i = Float64Index([0, 1.1, 2])
        result = i.astype(dtype)
        expected = Index(i.values.astype(dtype))
        tm.assert_index_equal(result, expected)
    for dtype in ['M8[ns]', 'm8[ns]']:
        msg = f'Cannot convert Float64Index to dtype {pandas_dtype(dtype)}; integer values are required for conversion'
        with pytest.raises(TypeError, match=re.escape(msg)):
            i.astype(dtype)
    for dtype in ['int16', 'int32', 'int64']:
        i = Float64Index([0, 1.1, np.NAN])
        msg = 'Cannot convert non-finite values \\(NA or inf\\) to integer'
        with pytest.raises(ValueError, match=msg):
            i.astype(dtype)