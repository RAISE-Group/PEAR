def test_pickle(self):
    v = Timedelta('1 days 10:11:12.0123456')
    v_p = tm.round_trip_pickle(v)
    assert v == v_p