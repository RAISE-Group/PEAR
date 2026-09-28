@pytest.mark.parametrize('dtype_class', [dict, Series])
def test_astype_dict_like(self, dtype_class):
    s = Series(range(0, 10, 2), name='abc')
    dt1 = dtype_class({'abc': str})
    result = s.astype(dt1)
    expected = Series(['0', '2', '4', '6', '8'], name='abc')
    tm.assert_series_equal(result, expected)
    dt2 = dtype_class({'abc': 'float64'})
    result = s.astype(dt2)
    expected = Series([0.0, 2.0, 4.0, 6.0, 8.0], dtype='float64', name='abc')
    tm.assert_series_equal(result, expected)
    dt3 = dtype_class({'abc': str, 'def': str})
    msg = 'Only the Series name can be used for the key in Series dtype mappings\\.'
    with pytest.raises(KeyError, match=msg):
        s.astype(dt3)
    dt4 = dtype_class({0: str})
    with pytest.raises(KeyError, match=msg):
        s.astype(dt4)
    if dtype_class is Series:
        dt5 = dtype_class({}, dtype=object)
    else:
        dt5 = dtype_class({})
    with pytest.raises(KeyError, match=msg):
        s.astype(dt5)