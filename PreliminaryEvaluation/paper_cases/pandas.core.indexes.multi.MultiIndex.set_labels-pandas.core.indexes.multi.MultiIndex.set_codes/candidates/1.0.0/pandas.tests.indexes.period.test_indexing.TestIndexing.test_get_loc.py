def test_get_loc(self):
    p0 = pd.Period('2017-09-01')
    p1 = pd.Period('2017-09-02')
    p2 = pd.Period('2017-09-03')
    idx0 = pd.PeriodIndex([p0, p1, p2])
    expected_idx1_p1 = 1
    expected_idx1_p2 = 2
    assert idx0.get_loc(p1) == expected_idx1_p1
    assert idx0.get_loc(str(p1)) == expected_idx1_p1
    assert idx0.get_loc(p2) == expected_idx1_p2
    assert idx0.get_loc(str(p2)) == expected_idx1_p2
    msg = "Cannot interpret 'foo' as period"
    with pytest.raises(KeyError, match=msg):
        idx0.get_loc('foo')
    with pytest.raises(KeyError, match='^1\\.1$'):
        idx0.get_loc(1.1)
    msg = "'PeriodIndex\\(\\['2017-09-01', '2017-09-02', '2017-09-03'\\], dtype='period\\[D\\]', freq='D'\\)' is an invalid key"
    with pytest.raises(TypeError, match=msg):
        idx0.get_loc(idx0)
    idx1 = pd.PeriodIndex([p1, p1, p2])
    expected_idx1_p1 = slice(0, 2)
    expected_idx1_p2 = 2
    assert idx1.get_loc(p1) == expected_idx1_p1
    assert idx1.get_loc(str(p1)) == expected_idx1_p1
    assert idx1.get_loc(p2) == expected_idx1_p2
    assert idx1.get_loc(str(p2)) == expected_idx1_p2
    msg = "Cannot interpret 'foo' as period"
    with pytest.raises(KeyError, match=msg):
        idx1.get_loc('foo')
    with pytest.raises(KeyError, match='^1\\.1$'):
        idx1.get_loc(1.1)
    msg = "'PeriodIndex\\(\\['2017-09-02', '2017-09-02', '2017-09-03'\\], dtype='period\\[D\\]', freq='D'\\)' is an invalid key"
    with pytest.raises(TypeError, match=msg):
        idx1.get_loc(idx1)
    idx2 = pd.PeriodIndex([p2, p1, p2])
    expected_idx2_p1 = 1
    expected_idx2_p2 = np.array([True, False, True])
    assert idx2.get_loc(p1) == expected_idx2_p1
    assert idx2.get_loc(str(p1)) == expected_idx2_p1
    tm.assert_numpy_array_equal(idx2.get_loc(p2), expected_idx2_p2)
    tm.assert_numpy_array_equal(idx2.get_loc(str(p2)), expected_idx2_p2)