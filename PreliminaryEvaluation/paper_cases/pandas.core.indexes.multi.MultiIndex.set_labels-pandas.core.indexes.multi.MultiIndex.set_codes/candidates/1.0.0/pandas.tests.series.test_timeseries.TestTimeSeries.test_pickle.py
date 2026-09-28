def test_pickle(self):
    p = tm.round_trip_pickle(NaT)
    assert p is NaT
    idx = pd.to_datetime(['2013-01-01', NaT, '2014-01-06'])
    idx_p = tm.round_trip_pickle(idx)
    assert idx_p[0] == idx[0]
    assert idx_p[1] is NaT
    assert idx_p[2] == idx[2]
    idx = date_range('1750-1-1', '2050-1-1', freq='7D')
    idx_p = tm.round_trip_pickle(idx)
    tm.assert_index_equal(idx, idx_p)