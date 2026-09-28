def test_dti_cmp_object_dtype(self):
    dti = date_range('2000-01-01', periods=10, tz='Asia/Tokyo')
    other = dti.astype('O')
    result = dti == other
    expected = np.array([True] * 10)
    tm.assert_numpy_array_equal(result, expected)
    other = dti.tz_localize(None)
    msg = 'Cannot compare tz-naive and tz-aware'
    with pytest.raises(TypeError, match=msg):
        dti != other
    other = np.array(list(dti[:5]) + [Timedelta(days=1)] * 5)
    result = dti == other
    expected = np.array([True] * 5 + [False] * 5)
    tm.assert_numpy_array_equal(result, expected)
    msg = 'Cannot compare type'
    with pytest.raises(TypeError, match=msg):
        dti >= other