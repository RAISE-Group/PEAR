def test_df_mod_zero_array(self):
    df = pd.DataFrame({'first': [3, 4, 5, 8], 'second': [0, 0, 0, 3]})
    first = pd.Series([0, 0, 0, 0], dtype='float64')
    second = pd.Series([np.nan, np.nan, np.nan, 0])
    expected = pd.DataFrame({'first': first, 'second': second})
    with np.errstate(all='ignore'):
        arr = df.values % df.values
    result2 = pd.DataFrame(arr, index=df.index, columns=df.columns, dtype='float64')
    result2.iloc[0:3, 1] = np.nan
    tm.assert_frame_equal(result2, expected)