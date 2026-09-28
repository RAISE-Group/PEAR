def test_multifunc_select_col_integer_cols(self, df):
    df.columns = np.arange(len(df.columns))
    df.groupby(1, as_index=False)[2].agg({'Q': np.mean})