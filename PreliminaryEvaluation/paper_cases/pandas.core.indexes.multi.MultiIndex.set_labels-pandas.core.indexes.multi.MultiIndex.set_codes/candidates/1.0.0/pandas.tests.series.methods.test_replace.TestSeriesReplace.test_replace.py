def test_replace(self, datetime_series):
    N = 100
    ser = pd.Series(np.random.randn(N))
    ser[0:4] = np.nan
    ser[6:10] = 0
    ser.replace([np.nan], -1, inplace=True)
    exp = ser.fillna(-1)
    tm.assert_series_equal(ser, exp)
    rs = ser.replace(0.0, np.nan)
    ser[ser == 0.0] = np.nan
    tm.assert_series_equal(rs, ser)
    ser = pd.Series(np.fabs(np.random.randn(N)), tm.makeDateIndex(N), dtype=object)
    ser[:5] = np.nan
    ser[6:10] = 'foo'
    ser[20:30] = 'bar'
    rs = ser.replace([np.nan, 'foo', 'bar'], -1)
    assert (rs[:5] == -1).all()
    assert (rs[6:10] == -1).all()
    assert (rs[20:30] == -1).all()
    assert pd.isna(ser[:5]).all()
    rs = ser.replace({np.nan: -1, 'foo': -2, 'bar': -3})
    assert (rs[:5] == -1).all()
    assert (rs[6:10] == -2).all()
    assert (rs[20:30] == -3).all()
    assert pd.isna(ser[:5]).all()
    rs2 = ser.replace([np.nan, 'foo', 'bar'], [-1, -2, -3])
    tm.assert_series_equal(rs, rs2)
    ser.replace([np.nan, 'foo', 'bar'], -1, inplace=True)
    assert (ser[:5] == -1).all()
    assert (ser[6:10] == -1).all()
    assert (ser[20:30] == -1).all()
    ser = pd.Series([np.nan, 0, np.inf])
    tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
    ser = pd.Series([np.nan, 0, 'foo', 'bar', np.inf, None, pd.NaT])
    tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
    filled = ser.copy()
    filled[4] = 0
    tm.assert_series_equal(ser.replace(np.inf, 0), filled)
    ser = pd.Series(datetime_series.index)
    tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
    msg = 'Replacement lists must match in length\\. Expecting 3 got 2'
    with pytest.raises(ValueError, match=msg):
        ser.replace([1, 2, 3], [np.nan, 0])
    with pytest.raises(TypeError, match='Cannot compare types .+'):
        ser.replace([1, 2], [np.nan, 0])
    ser = pd.Series([0, 1, 2, 3, 4])
    result = ser.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
    tm.assert_series_equal(result, pd.Series([4, 3, 2, 1, 0]))