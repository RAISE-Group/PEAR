def test_operators_timedelta64(self):
    v1 = pd.date_range('2012-1-1', periods=3, freq='D')
    v2 = pd.date_range('2012-1-2', periods=3, freq='D')
    rs = Series(v2) - Series(v1)
    xp = Series(1000000000.0 * 3600 * 24, rs.index).astype('int64').astype('timedelta64[ns]')
    tm.assert_series_equal(rs, xp)
    assert rs.dtype == 'timedelta64[ns]'
    df = DataFrame(dict(A=v1))
    td = Series([timedelta(days=i) for i in range(3)])
    assert td.dtype == 'timedelta64[ns]'
    result = df['A'] - df['A'].shift()
    assert result.dtype == 'timedelta64[ns]'
    result = df['A'] + td
    assert result.dtype == 'M8[ns]'
    maxa = df['A'].max()
    assert isinstance(maxa, Timestamp)
    resultb = df['A'] - df['A'].max()
    assert resultb.dtype == 'timedelta64[ns]'
    result = resultb + df['A']
    values = [Timestamp('20111230'), Timestamp('20120101'), Timestamp('20120103')]
    expected = Series(values, name='A')
    tm.assert_series_equal(result, expected)
    result = df['A'] - datetime(2001, 1, 1)
    expected = Series([timedelta(days=4017 + i) for i in range(3)], name='A')
    tm.assert_series_equal(result, expected)
    assert result.dtype == 'm8[ns]'
    d = datetime(2001, 1, 1, 3, 4)
    resulta = df['A'] - d
    assert resulta.dtype == 'm8[ns]'
    resultb = resulta + d
    tm.assert_series_equal(df['A'], resultb)
    td = timedelta(days=1)
    resulta = df['A'] + td
    resultb = resulta - td
    tm.assert_series_equal(resultb, df['A'])
    assert resultb.dtype == 'M8[ns]'
    td = timedelta(minutes=5, seconds=3)
    resulta = df['A'] + td
    resultb = resulta - td
    tm.assert_series_equal(df['A'], resultb)
    assert resultb.dtype == 'M8[ns]'
    value = rs[2] + np.timedelta64(timedelta(minutes=5, seconds=1))
    rs[2] += np.timedelta64(timedelta(minutes=5, seconds=1))
    assert rs[2] == value