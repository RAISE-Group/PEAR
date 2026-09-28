def test_set_index_timezone(self):
    idx = to_datetime(['2014-01-01 10:10:10'], utc=True).tz_convert('Europe/Rome')
    df = DataFrame({'A': idx})
    assert df.set_index(idx).index[0].hour == 11
    assert DatetimeIndex(Series(df.A))[0].hour == 11
    assert df.set_index(df.A).index[0].hour == 11