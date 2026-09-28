def test_union_dataframe_index(self):
    rng1 = pd.period_range('1/1/1999', '1/1/2012', freq='M')
    s1 = pd.Series(np.random.randn(len(rng1)), rng1)
    rng2 = pd.period_range('1/1/1980', '12/1/2001', freq='M')
    s2 = pd.Series(np.random.randn(len(rng2)), rng2)
    df = pd.DataFrame({'s1': s1, 's2': s2})
    exp = pd.period_range('1/1/1980', '1/1/2012', freq='M')
    tm.assert_index_equal(df.index, exp)