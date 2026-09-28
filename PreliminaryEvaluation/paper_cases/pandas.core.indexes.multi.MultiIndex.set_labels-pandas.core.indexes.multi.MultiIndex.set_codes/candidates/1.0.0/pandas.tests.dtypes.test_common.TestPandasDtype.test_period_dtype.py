@pytest.mark.parametrize('dtype', ['period[D]', 'period[3M]', 'period[U]', 'Period[D]', 'Period[3M]', 'Period[U]'])
def test_period_dtype(self, dtype):
    assert com.pandas_dtype(dtype) is PeriodDtype(dtype)
    assert com.pandas_dtype(dtype) == PeriodDtype(dtype)
    assert com.pandas_dtype(dtype) == dtype