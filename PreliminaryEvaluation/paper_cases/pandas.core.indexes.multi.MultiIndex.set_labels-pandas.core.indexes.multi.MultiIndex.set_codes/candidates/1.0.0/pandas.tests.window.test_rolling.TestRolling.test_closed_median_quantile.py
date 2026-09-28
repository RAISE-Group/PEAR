@pytest.mark.parametrize('closed,expected', [('right', [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8]), ('both', [0, 0.5, 1, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]), ('neither', [np.nan, 0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]), ('left', [np.nan, 0, 0.5, 1, 2, 3, 4, 5, 6, 7])])
def test_closed_median_quantile(self, closed, expected):
    ser = pd.Series(data=np.arange(10), index=pd.date_range('2000', periods=10))
    roll = ser.rolling('3D', closed=closed)
    expected = pd.Series(expected, index=ser.index)
    result = roll.median()
    tm.assert_series_equal(result, expected)
    result = roll.quantile(0.5)
    tm.assert_series_equal(result, expected)