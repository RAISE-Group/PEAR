def test_lookup_bool(self):
    df = DataFrame({'label': ['a', 'b', 'a', 'c'], 'mask_a': [True, True, False, True], 'mask_b': [True, False, False, False], 'mask_c': [False, True, False, True]})
    df['mask'] = df.lookup(df.index, 'mask_' + df['label'])
    exp_mask = np.array([df.loc[r, c] for r, c in zip(df.index, 'mask_' + df['label'])])
    tm.assert_series_equal(df['mask'], pd.Series(exp_mask, name='mask'))
    assert df['mask'].dtype == np.bool_