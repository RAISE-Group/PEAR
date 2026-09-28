@pytest.mark.parametrize('func', ['min', 'max'])
def test_closed_one_entry(self, func):
    ser = pd.Series(data=[2], index=pd.date_range('2000', periods=1))
    result = getattr(ser.rolling('10D', closed='left'), func)()
    tm.assert_series_equal(result, pd.Series([np.nan], index=ser.index))