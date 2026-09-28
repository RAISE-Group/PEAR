def test_NaT_scalar(self):
    series = Series([0, 1000, 2000, iNaT], dtype='M8[ns]')
    val = series[3]
    assert isna(val)
    series[2] = val
    assert isna(series[2])