def test_closed_uneven(self):
    ser = pd.Series(data=np.arange(10), index=pd.date_range('2000', periods=10))
    ser = ser.drop(index=ser.index[[1, 5]])
    result = ser.rolling('3D', closed='left').min()
    expected = pd.Series([np.nan, 0, 0, 2, 3, 4, 6, 6], index=ser.index)
    tm.assert_series_equal(result, expected)