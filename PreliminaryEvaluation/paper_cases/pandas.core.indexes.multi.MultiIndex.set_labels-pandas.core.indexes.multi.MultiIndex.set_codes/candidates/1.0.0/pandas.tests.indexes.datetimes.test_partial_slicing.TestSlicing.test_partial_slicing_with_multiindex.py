def test_partial_slicing_with_multiindex(self):
    df = DataFrame({'ACCOUNT': ['ACCT1', 'ACCT1', 'ACCT1', 'ACCT2'], 'TICKER': ['ABC', 'MNP', 'XYZ', 'XYZ'], 'val': [1, 2, 3, 4]}, index=date_range('2013-06-19 09:30:00', periods=4, freq='5T'))
    df_multi = df.set_index(['ACCOUNT', 'TICKER'], append=True)
    expected = DataFrame([[1]], index=Index(['ABC'], name='TICKER'), columns=['val'])
    result = df_multi.loc['2013-06-19 09:30:00', 'ACCT1']
    tm.assert_frame_equal(result, expected)
    expected = df_multi.loc[pd.Timestamp('2013-06-19 09:30:00', tz=None), 'ACCT1', 'ABC']
    result = df_multi.loc['2013-06-19 09:30:00', 'ACCT1', 'ABC']
    tm.assert_series_equal(result, expected)
    msg = 'Too many indexers'
    with pytest.raises(IndexingError, match=msg):
        df_multi.loc['2013-06-19', 'ACCT1', 'ABC']
    s = pd.DataFrame(np.random.rand(1000, 1000), index=pd.date_range('2000-1-1', periods=1000)).stack()
    s2 = s[:-1].copy()
    expected = s2['2000-1-4']
    result = s2[pd.Timestamp('2000-1-4')]
    tm.assert_series_equal(result, expected)
    result = s[pd.Timestamp('2000-1-4')]
    expected = s['2000-1-4']
    tm.assert_series_equal(result, expected)
    df2 = pd.DataFrame(s)
    expected = df2.xs('2000-1-4')
    result = df2.loc[pd.Timestamp('2000-1-4')]
    tm.assert_frame_equal(result, expected)