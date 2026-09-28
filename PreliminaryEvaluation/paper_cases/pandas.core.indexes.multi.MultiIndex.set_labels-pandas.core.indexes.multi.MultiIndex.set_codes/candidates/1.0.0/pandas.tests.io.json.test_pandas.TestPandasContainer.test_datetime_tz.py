def test_datetime_tz(self):
    tz_range = pd.date_range('20130101', periods=3, tz='US/Eastern')
    tz_naive = tz_range.tz_convert('utc').tz_localize(None)
    df = DataFrame({'A': tz_range, 'B': pd.date_range('20130101', periods=3)})
    df_naive = df.copy()
    df_naive['A'] = tz_naive
    expected = df_naive.to_json()
    assert expected == df.to_json()
    stz = Series(tz_range)
    s_naive = Series(tz_naive)
    assert stz.to_json() == s_naive.to_json()