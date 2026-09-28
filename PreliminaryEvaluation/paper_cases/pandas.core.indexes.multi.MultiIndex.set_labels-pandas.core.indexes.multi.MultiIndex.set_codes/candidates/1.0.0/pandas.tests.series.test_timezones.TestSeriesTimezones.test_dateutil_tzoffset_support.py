def test_dateutil_tzoffset_support(self):
    values = [188.5, 328.25]
    tzinfo = tzoffset(None, 7200)
    index = [datetime(2012, 5, 11, 11, tzinfo=tzinfo), datetime(2012, 5, 11, 12, tzinfo=tzinfo)]
    series = Series(data=values, index=index)
    assert series.index.tz == tzinfo
    repr(series.index[0])