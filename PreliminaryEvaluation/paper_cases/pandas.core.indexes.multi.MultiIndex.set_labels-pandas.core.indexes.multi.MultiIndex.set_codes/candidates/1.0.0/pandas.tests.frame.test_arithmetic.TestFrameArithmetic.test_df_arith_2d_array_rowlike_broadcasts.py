def test_df_arith_2d_array_rowlike_broadcasts(self, all_arithmetic_operators):
    opname = all_arithmetic_operators
    arr = np.arange(6).reshape(3, 2)
    df = pd.DataFrame(arr, columns=[True, False], index=['A', 'B', 'C'])
    rowlike = arr[[1], :]
    assert rowlike.shape == (1, df.shape[1])
    exvals = [getattr(df.loc['A'], opname)(rowlike.squeeze()), getattr(df.loc['B'], opname)(rowlike.squeeze()), getattr(df.loc['C'], opname)(rowlike.squeeze())]
    expected = pd.DataFrame(exvals, columns=df.columns, index=df.index)
    if opname in ['__rmod__', '__rfloordiv__']:
        expected[False] = expected[False].astype(exvals[-1].dtype)
    result = getattr(df, opname)(rowlike)
    tm.assert_frame_equal(result, expected)