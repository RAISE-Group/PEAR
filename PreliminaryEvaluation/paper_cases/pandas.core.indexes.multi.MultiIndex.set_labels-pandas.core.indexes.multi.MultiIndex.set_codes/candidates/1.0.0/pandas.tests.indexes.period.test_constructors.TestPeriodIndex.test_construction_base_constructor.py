def test_construction_base_constructor(self):
    arr = [pd.Period('2011-01', freq='M'), pd.NaT, pd.Period('2011-03', freq='M')]
    tm.assert_index_equal(pd.Index(arr), pd.PeriodIndex(arr))
    tm.assert_index_equal(pd.Index(np.array(arr)), pd.PeriodIndex(np.array(arr)))
    arr = [np.nan, pd.NaT, pd.Period('2011-03', freq='M')]
    tm.assert_index_equal(pd.Index(arr), pd.PeriodIndex(arr))
    tm.assert_index_equal(pd.Index(np.array(arr)), pd.PeriodIndex(np.array(arr)))
    arr = [pd.Period('2011-01', freq='M'), pd.NaT, pd.Period('2011-03', freq='D')]
    tm.assert_index_equal(pd.Index(arr), pd.Index(arr, dtype=object))
    tm.assert_index_equal(pd.Index(np.array(arr)), pd.Index(np.array(arr), dtype=object))