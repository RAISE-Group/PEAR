def test_construction_base_constructor(self):
    arr = [pd.Timestamp('2011-01-01'), pd.NaT, pd.Timestamp('2011-01-03')]
    tm.assert_index_equal(pd.Index(arr), pd.DatetimeIndex(arr))
    tm.assert_index_equal(pd.Index(np.array(arr)), pd.DatetimeIndex(np.array(arr)))
    arr = [np.nan, pd.NaT, pd.Timestamp('2011-01-03')]
    tm.assert_index_equal(pd.Index(arr), pd.DatetimeIndex(arr))
    tm.assert_index_equal(pd.Index(np.array(arr)), pd.DatetimeIndex(np.array(arr)))