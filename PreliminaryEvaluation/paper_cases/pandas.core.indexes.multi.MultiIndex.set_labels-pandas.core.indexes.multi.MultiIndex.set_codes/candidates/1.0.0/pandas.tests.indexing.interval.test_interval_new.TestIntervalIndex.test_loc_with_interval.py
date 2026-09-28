def test_loc_with_interval(self):
    s = self.s
    expected = 0
    result = s.loc[Interval(0, 1)]
    assert result == expected
    result = s[Interval(0, 1)]
    assert result == expected
    expected = s.iloc[3:5]
    result = s.loc[[Interval(3, 4), Interval(4, 5)]]
    tm.assert_series_equal(expected, result)
    result = s[[Interval(3, 4), Interval(4, 5)]]
    tm.assert_series_equal(expected, result)
    with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='left')")):
        s.loc[Interval(3, 5, closed='left')]
    with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='left')")):
        s[Interval(3, 5, closed='left')]
    with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
        s[Interval(3, 5)]
    with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
        s.loc[Interval(3, 5)]
    with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
        s[Interval(3, 5)]
    with pytest.raises(KeyError, match=re.escape("Interval(-2, 0, closed='right')")):
        s.loc[Interval(-2, 0)]
    with pytest.raises(KeyError, match=re.escape("Interval(-2, 0, closed='right')")):
        s[Interval(-2, 0)]
    with pytest.raises(KeyError, match=re.escape("Interval(5, 6, closed='right')")):
        s.loc[Interval(5, 6)]
    with pytest.raises(KeyError, match=re.escape("Interval(5, 6, closed='right')")):
        s[Interval(5, 6)]