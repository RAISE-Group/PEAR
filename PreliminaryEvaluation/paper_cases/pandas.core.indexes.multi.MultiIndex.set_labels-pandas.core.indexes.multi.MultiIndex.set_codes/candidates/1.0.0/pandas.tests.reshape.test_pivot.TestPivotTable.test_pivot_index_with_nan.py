@pytest.mark.parametrize('method', [True, False])
def test_pivot_index_with_nan(self, method):
    nan = np.nan
    df = DataFrame({'a': ['R1', 'R2', nan, 'R4'], 'b': ['C1', 'C2', 'C3', 'C4'], 'c': [10, 15, 17, 20]})
    if method:
        result = df.pivot('a', 'b', 'c')
    else:
        result = pd.pivot(df, 'a', 'b', 'c')
    expected = DataFrame([[nan, nan, 17, nan], [10, nan, nan, nan], [nan, 15, nan, nan], [nan, nan, nan, 20]], index=Index([nan, 'R1', 'R2', 'R4'], name='a'), columns=Index(['C1', 'C2', 'C3', 'C4'], name='b'))
    tm.assert_frame_equal(result, expected)
    tm.assert_frame_equal(df.pivot('b', 'a', 'c'), expected.T)
    df = DataFrame({'a': pd.date_range('2014-02-01', periods=6, freq='D'), 'c': 100 + np.arange(6)})
    df['b'] = df['a'] - pd.Timestamp('2014-02-02')
    df.loc[1, 'a'] = df.loc[3, 'a'] = nan
    df.loc[1, 'b'] = df.loc[4, 'b'] = nan
    if method:
        pv = df.pivot('a', 'b', 'c')
    else:
        pv = pd.pivot(df, 'a', 'b', 'c')
    assert pv.notna().values.sum() == len(df)
    for _, row in df.iterrows():
        assert pv.loc[row['a'], row['b']] == row['c']
    if method:
        result = df.pivot('b', 'a', 'c')
    else:
        result = pd.pivot(df, 'b', 'a', 'c')
    tm.assert_frame_equal(result, pv.T)