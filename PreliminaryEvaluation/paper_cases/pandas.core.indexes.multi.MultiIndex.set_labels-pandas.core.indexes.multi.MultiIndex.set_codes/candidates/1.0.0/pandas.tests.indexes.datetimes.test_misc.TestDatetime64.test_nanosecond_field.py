def test_nanosecond_field(self):
    dti = DatetimeIndex(np.arange(10))
    tm.assert_index_equal(dti.nanosecond, pd.Index(np.arange(10, dtype=np.int64)))