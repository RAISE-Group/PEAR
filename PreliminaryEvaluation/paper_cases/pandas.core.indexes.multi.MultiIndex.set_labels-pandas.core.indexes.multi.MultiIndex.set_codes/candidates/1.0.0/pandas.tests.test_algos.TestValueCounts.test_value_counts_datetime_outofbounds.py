def test_value_counts_datetime_outofbounds(self):
    s = Series([datetime(3000, 1, 1), datetime(5000, 1, 1), datetime(5000, 1, 1), datetime(6000, 1, 1), datetime(3000, 1, 1), datetime(3000, 1, 1)])
    res = s.value_counts()
    exp_index = Index([datetime(3000, 1, 1), datetime(5000, 1, 1), datetime(6000, 1, 1)], dtype=object)
    exp = Series([3, 2, 1], index=exp_index)
    tm.assert_series_equal(res, exp)
    res = pd.to_datetime(Series(['2362-01-01', np.nan]), errors='ignore')
    exp = Series(['2362-01-01', np.nan], dtype=object)
    tm.assert_series_equal(res, exp)