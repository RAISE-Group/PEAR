def test_empty_series_add_sub(self):
    a = Series(dtype='M8[ns]')
    b = Series(dtype='m8[ns]')
    tm.assert_series_equal(a, a + b)
    tm.assert_series_equal(a, a - b)
    tm.assert_series_equal(a, b + a)
    msg = 'cannot subtract'
    with pytest.raises(TypeError, match=msg):
        b - a