def test_count(self):
    frame = self.frame.copy()
    frame.index.names = ['a', 'b']
    result = frame.count(level='b')
    expect = self.frame.count(level=1)
    tm.assert_frame_equal(result, expect, check_names=False)
    result = frame.count(level='a')
    expect = self.frame.count(level=0)
    tm.assert_frame_equal(result, expect, check_names=False)
    series = self.series.copy()
    series.index.names = ['a', 'b']
    result = series.count(level='b')
    expect = self.series.count(level=1).rename_axis('b')
    tm.assert_series_equal(result, expect)
    result = series.count(level='a')
    expect = self.series.count(level=0).rename_axis('a')
    tm.assert_series_equal(result, expect)
    msg = 'Level x not found'
    with pytest.raises(KeyError, match=msg):
        series.count('x')
    with pytest.raises(KeyError, match=msg):
        frame.count(level='x')