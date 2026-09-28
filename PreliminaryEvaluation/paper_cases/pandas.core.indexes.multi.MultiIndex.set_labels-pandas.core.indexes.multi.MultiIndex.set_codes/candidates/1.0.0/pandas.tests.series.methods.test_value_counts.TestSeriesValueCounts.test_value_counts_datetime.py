def test_value_counts_datetime(self):
    values = [pd.Timestamp('2011-01-01 09:00'), pd.Timestamp('2011-01-01 10:00'), pd.Timestamp('2011-01-01 11:00'), pd.Timestamp('2011-01-01 09:00'), pd.Timestamp('2011-01-01 09:00'), pd.Timestamp('2011-01-01 11:00')]
    exp_idx = pd.DatetimeIndex(['2011-01-01 09:00', '2011-01-01 11:00', '2011-01-01 10:00'])
    exp = pd.Series([3, 2, 1], index=exp_idx, name='xxx')
    ser = pd.Series(values, name='xxx')
    tm.assert_series_equal(ser.value_counts(), exp)
    idx = pd.DatetimeIndex(values, name='xxx')
    tm.assert_series_equal(idx.value_counts(), exp)
    exp = pd.Series(np.array([3.0, 2.0, 1]) / 6.0, index=exp_idx, name='xxx')
    tm.assert_series_equal(ser.value_counts(normalize=True), exp)
    tm.assert_series_equal(idx.value_counts(normalize=True), exp)