def test_comparison_object_array(self):
    ts = Timestamp('2011-01-03 00:00:00-0500', tz='US/Eastern')
    other = Timestamp('2011-01-01 00:00:00-0500', tz='US/Eastern')
    naive = Timestamp('2011-01-01 00:00:00')
    arr = np.array([other, ts], dtype=object)
    res = arr == ts
    expected = np.array([False, True], dtype=bool)
    assert (res == expected).all()
    arr = np.array([[other, ts], [ts, other]], dtype=object)
    res = arr != ts
    expected = np.array([[True, False], [False, True]], dtype=bool)
    assert res.shape == expected.shape
    assert (res == expected).all()
    arr = np.array([naive], dtype=object)
    with pytest.raises(TypeError):
        arr < ts