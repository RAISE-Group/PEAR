def test_pickle(self, mgr):
    mgr2 = tm.round_trip_pickle(mgr)
    tm.assert_frame_equal(DataFrame(mgr), DataFrame(mgr2))
    assert hasattr(mgr2, '_is_consolidated')
    assert hasattr(mgr2, '_known_consolidated')
    assert not mgr2._is_consolidated
    assert not mgr2._known_consolidated