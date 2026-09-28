def test_write_preserves_original(self):
    np.random.seed(423)
    df = pd.DataFrame(np.random.randn(5, 4), columns=list('abcd'))
    df.loc[2, 'a':'c'] = np.nan
    df_copy = df.copy()
    with tm.ensure_clean() as path:
        df.to_stata(path, write_index=False)
    tm.assert_frame_equal(df, df_copy)