def test_to_frame(self, datetime_series):
    datetime_series.name = None
    rs = datetime_series.to_frame()
    xp = pd.DataFrame(datetime_series.values, index=datetime_series.index)
    tm.assert_frame_equal(rs, xp)
    datetime_series.name = 'testname'
    rs = datetime_series.to_frame()
    xp = pd.DataFrame(dict(testname=datetime_series.values), index=datetime_series.index)
    tm.assert_frame_equal(rs, xp)
    rs = datetime_series.to_frame(name='testdifferent')
    xp = pd.DataFrame(dict(testdifferent=datetime_series.values), index=datetime_series.index)
    tm.assert_frame_equal(rs, xp)