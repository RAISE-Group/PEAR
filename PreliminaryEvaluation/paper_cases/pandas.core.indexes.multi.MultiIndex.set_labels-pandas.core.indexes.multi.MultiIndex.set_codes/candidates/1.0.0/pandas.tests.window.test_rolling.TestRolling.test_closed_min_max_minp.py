@pytest.mark.parametrize('func,closed,expected', [('min', 'right', [np.nan, 0, 0, 1, 2, 3, 4, 5, np.nan, np.nan]), ('min', 'both', [np.nan, 0, 0, 0, 1, 2, 3, 4, 5, np.nan]), ('min', 'neither', [np.nan, np.nan, 0, 1, 2, 3, 4, 5, np.nan, np.nan]), ('min', 'left', [np.nan, np.nan, 0, 0, 1, 2, 3, 4, 5, np.nan]), ('max', 'right', [np.nan, 1, 2, 3, 4, 5, 6, 6, np.nan, np.nan]), ('max', 'both', [np.nan, 1, 2, 3, 4, 5, 6, 6, 6, np.nan]), ('max', 'neither', [np.nan, np.nan, 1, 2, 3, 4, 5, 6, np.nan, np.nan]), ('max', 'left', [np.nan, np.nan, 1, 2, 3, 4, 5, 6, 6, np.nan])])
def test_closed_min_max_minp(self, func, closed, expected):
    ser = pd.Series(data=np.arange(10), index=pd.date_range('2000', periods=10))
    ser[ser.index[-3:]] = np.nan
    result = getattr(ser.rolling('3D', min_periods=2, closed=closed), func)()
    expected = pd.Series(expected, index=ser.index)
    tm.assert_series_equal(result, expected)