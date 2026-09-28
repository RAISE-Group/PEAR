def test_dti_union_mixed(self):
    rng = DatetimeIndex([pd.Timestamp('2011-01-01'), pd.NaT])
    rng2 = pd.DatetimeIndex(['2012-01-01', '2012-01-02'], tz='Asia/Tokyo')
    result = rng.union(rng2)
    expected = Index([pd.Timestamp('2011-01-01'), pd.NaT, pd.Timestamp('2012-01-01', tz='Asia/Tokyo'), pd.Timestamp('2012-01-02', tz='Asia/Tokyo')], dtype=object)
    tm.assert_index_equal(result, expected)