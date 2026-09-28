@pytest.mark.parametrize('start_date', ['2017-01-01 23:59:59.999999999', '2017-01-01 23:59:59.99999999', '2017-01-01 23:59:59.9999999', '2017-01-01 23:59:59.999999', '2017-01-01 23:59:59.99999', '2017-01-01 23:59:59.9999'])
def test_datetimeindex_highprecision(self, start_date):
    df = DataFrame({'A': date_range(start=start_date, freq='D', periods=5)})
    result = str(df)
    assert start_date in result
    dti = date_range(start=start_date, freq='D', periods=5)
    df = DataFrame({'A': range(5)}, index=dti)
    result = str(df.index)
    assert start_date in result