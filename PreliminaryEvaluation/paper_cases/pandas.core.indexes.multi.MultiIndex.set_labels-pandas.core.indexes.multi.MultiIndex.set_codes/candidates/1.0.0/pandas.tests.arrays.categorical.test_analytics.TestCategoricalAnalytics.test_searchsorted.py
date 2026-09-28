def test_searchsorted(self, ordered_fixture):
    cat = Categorical(['cheese', 'milk', 'apple', 'bread', 'bread'], categories=['cheese', 'milk', 'apple', 'bread'], ordered=ordered_fixture)
    ser = Series(cat)
    res_cat = cat.searchsorted('apple')
    assert res_cat == 2
    assert is_scalar(res_cat)
    res_ser = ser.searchsorted('apple')
    assert res_ser == 2
    assert is_scalar(res_ser)
    res_cat = cat.searchsorted(['bread'])
    res_ser = ser.searchsorted(['bread'])
    exp = np.array([3], dtype=np.intp)
    tm.assert_numpy_array_equal(res_cat, exp)
    tm.assert_numpy_array_equal(res_ser, exp)
    res_cat = cat.searchsorted(['apple', 'bread'], side='right')
    res_ser = ser.searchsorted(['apple', 'bread'], side='right')
    exp = np.array([3, 5], dtype=np.intp)
    tm.assert_numpy_array_equal(res_cat, exp)
    tm.assert_numpy_array_equal(res_ser, exp)
    with pytest.raises(KeyError, match='cucumber'):
        cat.searchsorted('cucumber')
    with pytest.raises(KeyError, match='cucumber'):
        ser.searchsorted('cucumber')
    with pytest.raises(KeyError, match='cucumber'):
        cat.searchsorted(['bread', 'cucumber'])
    with pytest.raises(KeyError, match='cucumber'):
        ser.searchsorted(['bread', 'cucumber'])