@pytest.mark.parametrize('dtype', [str, np.str_])
@pytest.mark.parametrize('series', [Series([string.digits * 10, tm.rands(63), tm.rands(64), tm.rands(1000)]), Series([string.digits * 10, tm.rands(63), tm.rands(64), np.nan, 1.0])])
def test_astype_str_map(self, dtype, series):
    result = series.astype(dtype)
    expected = series.map(str)
    tm.assert_series_equal(result, expected)