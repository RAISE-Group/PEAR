def test_ndarray(self):
    values = np.array([1, 2, 3])
    assert np.allclose(nanops._ensure_numeric(values), values)
    o_values = values.astype(object)
    assert np.allclose(nanops._ensure_numeric(o_values), values)
    s_values = np.array(['1', '2', '3'], dtype=object)
    assert np.allclose(nanops._ensure_numeric(s_values), values)
    s_values = np.array(['foo', 'bar', 'baz'], dtype=object)
    msg = "could not convert string to float: '(foo|baz)'"
    with pytest.raises(ValueError, match=msg):
        nanops._ensure_numeric(s_values)