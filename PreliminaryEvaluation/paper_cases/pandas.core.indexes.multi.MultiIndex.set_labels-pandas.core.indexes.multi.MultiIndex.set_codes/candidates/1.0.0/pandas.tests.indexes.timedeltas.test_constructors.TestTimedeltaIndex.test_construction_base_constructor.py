def test_construction_base_constructor(self):
    arr = [pd.Timedelta('1 days'), pd.NaT, pd.Timedelta('3 days')]
    tm.assert_index_equal(pd.Index(arr), pd.TimedeltaIndex(arr))
    tm.assert_index_equal(pd.Index(np.array(arr)), pd.TimedeltaIndex(np.array(arr)))
    arr = [np.nan, pd.NaT, pd.Timedelta('1 days')]
    tm.assert_index_equal(pd.Index(arr), pd.TimedeltaIndex(arr))
    tm.assert_index_equal(pd.Index(np.array(arr)), pd.TimedeltaIndex(np.array(arr)))