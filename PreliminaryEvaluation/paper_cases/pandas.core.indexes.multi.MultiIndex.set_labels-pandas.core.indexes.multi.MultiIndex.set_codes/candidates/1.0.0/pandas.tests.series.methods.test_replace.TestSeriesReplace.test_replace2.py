def test_replace2(self):
    N = 100
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