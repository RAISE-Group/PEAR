def test_df_arith_2d_array_collike_broadcasts(self, all_arithmetic_operators):
    opname = all_arithmetic_operators
    arr = np.arange(6).reshape(3, 2)
    df = pd.DataFrame(arr, columns=[True, False], index=['A', 'B', 'C'])
    collike = arr[:, [1]]
    assert collike.shape == (df.shape[0], 1)
    exvals = {True: getattr(df[True], opname)(collike.squeeze()), False: getattr(df[False], opname)(collike.squeeze())}
    dtype = None
    if opname in ['__rmod__', '__rfloordiv__']:
        dtype = np.common_type(*[x.values for x in exvals.values()])
    expected = pd.DataFrame(exvals, columns=df.columns, index=df.index, dtype=dtype)
    result = getattr(df, opname)(collike)
    tm.assert_frame_equal(result, expected)