@pytest.mark.parametrize('cache', [True, False])
def test_dataframe(self, cache):
    df = DataFrame({'year': [2015, 2016], 'month': [2, 3], 'day': [4, 5], 'hour': [6, 7], 'minute': [58, 59], 'second': [10, 11], 'ms': [1, 1], 'us': [2, 2], 'ns': [3, 3]})
    result = to_datetime({'year': df['year'], 'month': df['month'], 'day': df['day']}, cache=cache)
    expected = Series([Timestamp('20150204 00:00:00'), Timestamp('20160305 00:0:00')])
    tm.assert_series_equal(result, expected)
    result = to_datetime(df[['year', 'month', 'day']].to_dict(), cache=cache)
    tm.assert_series_equal(result, expected)
    df2 = df[['year', 'month', 'day']].to_dict()
    df2['month'] = 2
    result = to_datetime(df2, cache=cache)
    expected2 = Series([Timestamp('20150204 00:00:00'), Timestamp('20160205 00:0:00')])
    tm.assert_series_equal(result, expected2)
    units = [{'year': 'years', 'month': 'months', 'day': 'days', 'hour': 'hours', 'minute': 'minutes', 'second': 'seconds'}, {'year': 'year', 'month': 'month', 'day': 'day', 'hour': 'hour', 'minute': 'minute', 'second': 'second'}]
    for d in units:
        result = to_datetime(df[list(d.keys())].rename(columns=d), cache=cache)
        expected = Series([Timestamp('20150204 06:58:10'), Timestamp('20160305 07:59:11')])
        tm.assert_series_equal(result, expected)
    d = {'year': 'year', 'month': 'month', 'day': 'day', 'hour': 'hour', 'minute': 'minute', 'second': 'second', 'ms': 'ms', 'us': 'us', 'ns': 'ns'}
    result = to_datetime(df.rename(columns=d), cache=cache)
    expected = Series([Timestamp('20150204 06:58:10.001002003'), Timestamp('20160305 07:59:11.001002003')])
    tm.assert_series_equal(result, expected)
    result = to_datetime(df.astype(str), cache=cache)
    tm.assert_series_equal(result, expected)
    df2 = DataFrame({'year': [2015, 2016], 'month': [2, 20], 'day': [4, 5]})
    msg = "cannot assemble the datetimes: time data .+ does not match format '%Y%m%d' \\(match\\)"
    with pytest.raises(ValueError, match=msg):
        to_datetime(df2, cache=cache)
    result = to_datetime(df2, errors='coerce', cache=cache)
    expected = Series([Timestamp('20150204 00:00:00'), NaT])
    tm.assert_series_equal(result, expected)
    msg = 'extra keys have been passed to the datetime assemblage: \\[foo\\]'
    with pytest.raises(ValueError, match=msg):
        df2 = df.copy()
        df2['foo'] = 1
        to_datetime(df2, cache=cache)
    msg = 'to assemble mappings requires at least that \\[year, month, day\\] be specified: \\[.+\\] is missing'
    for c in [['year'], ['year', 'month'], ['year', 'month', 'second'], ['month', 'day'], ['year', 'day', 'second']]:
        with pytest.raises(ValueError, match=msg):
            to_datetime(df[c], cache=cache)
    msg = 'cannot assemble with duplicate keys'
    df2 = DataFrame({'year': [2015, 2016], 'month': [2, 20], 'day': [4, 5]})
    df2.columns = ['year', 'year', 'day']
    with pytest.raises(ValueError, match=msg):
        to_datetime(df2, cache=cache)
    df2 = DataFrame({'year': [2015, 2016], 'month': [2, 20], 'day': [4, 5], 'hour': [4, 5]})
    df2.columns = ['year', 'month', 'day', 'day']
    with pytest.raises(ValueError, match=msg):
        to_datetime(df2, cache=cache)