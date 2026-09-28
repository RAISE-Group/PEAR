def test_at_iat_coercion(self):
    dates = date_range('1/1/2000', periods=8)
    df = DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
    s = df['A']
    result = s.at[dates[5]]
    xp = s.values[5]
    assert result == xp
    s = Series(['2014-01-01', '2014-02-02'], dtype='datetime64[ns]')
    expected = Timestamp('2014-02-02')
    for r in [lambda: s.iat[1], lambda: s.iloc[1]]:
        result = r()
        assert result == expected
    s = Series(['1 days', '2 days'], dtype='timedelta64[ns]')
    expected = Timedelta('2 days')
    for r in [lambda: s.iat[1], lambda: s.iloc[1]]:
        result = r()
        assert result == expected