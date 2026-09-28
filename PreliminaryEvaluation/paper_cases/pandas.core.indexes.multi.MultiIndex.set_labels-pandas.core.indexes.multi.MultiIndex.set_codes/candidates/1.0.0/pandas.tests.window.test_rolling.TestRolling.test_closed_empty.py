@pytest.mark.parametrize('closed', ['neither', 'left'])
def test_closed_empty(self, closed, arithmetic_win_operators):
    func_name = arithmetic_win_operators
    ser = pd.Series(data=np.arange(5), index=pd.date_range('2000', periods=5, freq='2D'))
    roll = ser.rolling('1D', closed=closed)
    result = getattr(roll, func_name)()
    expected = pd.Series([np.nan] * 5, index=ser.index)
    tm.assert_series_equal(result, expected)