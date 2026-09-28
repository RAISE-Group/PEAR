def test_non_unique_pickle(self):
    mgr = create_mgr('a,a,a:f8')
    mgr2 = tm.round_trip_pickle(mgr)
    tm.assert_frame_equal(DataFrame(mgr), DataFrame(mgr2))
    mgr = create_mgr('a: f8; a: i8')
    mgr2 = tm.round_trip_pickle(mgr)
    tm.assert_frame_equal(DataFrame(mgr), DataFrame(mgr2))