@pytest.mark.xfail(reason='PeriodDtype Series not supported yet')
def test_NaT_scalar(self):
    series = Series([0, 1000, 2000, pd._libs.iNaT], dtype='period[D]')
    val = series[3]
    assert pd.isna(val)
    series[2] = val
    assert pd.isna(series[2])