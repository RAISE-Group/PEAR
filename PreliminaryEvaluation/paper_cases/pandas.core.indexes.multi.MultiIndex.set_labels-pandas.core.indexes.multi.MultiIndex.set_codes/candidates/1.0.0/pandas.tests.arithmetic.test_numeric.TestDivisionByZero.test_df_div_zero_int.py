def test_df_div_zero_int(self):
    df = pd.DataFrame({'first': [3, 4, 5, 8], 'second': [0, 0, 0, 3]})
    result = df / 0
    expected = pd.DataFrame(np.inf, index=df.index, columns=df.columns)
    expected.iloc[0:3, 1] = np.nan
    tm.assert_frame_equal(result, expected)
    with np.errstate(all='ignore'):
        arr = df.values.astype('float64') / 0
    result2 = pd.DataFrame(arr, index=df.index, columns=df.columns)
    tm.assert_frame_equal(result2, expected)