def test_round_trip(self):
    p = Period('2000Q1')
    new_p = tm.round_trip_pickle(p)
    assert new_p == p