@pytest.mark.parametrize('start,stop, expected_slice', [[np.timedelta64(0, 'ns'), None, slice(0, 11)], [np.timedelta64(1, 'D'), np.timedelta64(6, 'D'), slice(1, 7)], [None, np.timedelta64(4, 'D'), slice(0, 5)]])
def test_numpy_timedelta_scalar_indexing(self, start, stop, expected_slice):
    s = pd.Series(range(11), pd.timedelta_range('0 days', '10 days'))
    result = s.loc[slice(start, stop)]
    expected = s.iloc[expected_slice]
    tm.assert_series_equal(result, expected)