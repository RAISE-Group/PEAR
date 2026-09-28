def test_crosstab_with_empties(self):
    df = pd.DataFrame({'a': [1, 2, 2, 2, 2], 'b': [3, 3, 4, 4, 4], 'c': [np.nan, np.nan, np.nan, np.nan, np.nan]})
    empty = pd.DataFrame([[0.0, 0.0], [0.0, 0.0]], index=pd.Index([1, 2], name='a', dtype='int64'), columns=pd.Index([3, 4], name='b'))
    for i in [True, 'index', 'columns']:
        calculated = pd.crosstab(df.a, df.b, values=df.c, aggfunc='count', normalize=i)
        tm.assert_frame_equal(empty, calculated)
    nans = pd.DataFrame([[0.0, np.nan], [0.0, 0.0]], index=pd.Index([1, 2], name='a', dtype='int64'), columns=pd.Index([3, 4], name='b'))
    calculated = pd.crosstab(df.a, df.b, values=df.c, aggfunc='count', normalize=False)
    tm.assert_frame_equal(nans, calculated)