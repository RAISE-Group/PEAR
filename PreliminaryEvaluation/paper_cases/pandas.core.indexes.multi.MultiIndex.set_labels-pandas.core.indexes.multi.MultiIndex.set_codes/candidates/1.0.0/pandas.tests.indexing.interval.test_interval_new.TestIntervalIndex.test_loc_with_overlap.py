def test_loc_with_overlap(self):
    idx = IntervalIndex.from_tuples([(1, 5), (3, 7)])
    s = Series(range(len(idx)), index=idx)
    expected = s
    result = s.loc[4]
    tm.assert_series_equal(expected, result)
    result = s[4]
    tm.assert_series_equal(expected, result)
    result = s.loc[[4]]
    tm.assert_series_equal(expected, result)
    result = s[[4]]
    tm.assert_series_equal(expected, result)
    expected = 0
    result = s.loc[Interval(1, 5)]
    result == expected
    result = s[Interval(1, 5)]
    result == expected
    expected = s
    result = s.loc[[Interval(1, 5), Interval(3, 7)]]
    tm.assert_series_equal(expected, result)
    result = s[[Interval(1, 5), Interval(3, 7)]]
    tm.assert_series_equal(expected, result)
    with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
        s.loc[Interval(3, 5)]
    with pytest.raises(KeyError, match='^$'):
        s.loc[[Interval(3, 5)]]
    with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
        s[Interval(3, 5)]
    with pytest.raises(KeyError, match='^$'):
        s[[Interval(3, 5)]]
    expected = s
    result = s.loc[Interval(1, 5):Interval(3, 7)]
    tm.assert_series_equal(expected, result)
    result = s[Interval(1, 5):Interval(3, 7)]
    tm.assert_series_equal(expected, result)
    msg = "'can only get slices from an IntervalIndex if bounds are"
    " non-overlapping and all monotonic increasing or decreasing'"
    with pytest.raises(KeyError, match=msg):
        s.loc[Interval(1, 6):Interval(3, 8)]
    with pytest.raises(KeyError, match=msg):
        s[Interval(1, 6):Interval(3, 8)]
    with pytest.raises(KeyError, match=msg):
        s.loc[1:4]