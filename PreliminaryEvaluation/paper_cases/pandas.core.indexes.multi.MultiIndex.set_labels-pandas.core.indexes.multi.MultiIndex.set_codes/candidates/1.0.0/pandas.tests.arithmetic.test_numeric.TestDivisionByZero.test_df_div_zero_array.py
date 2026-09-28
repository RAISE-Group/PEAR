def test_df_div_zero_array(self):
    df = pd.DataFrame({'first': [3, 4, 5, 8], 'second': [0, 0, 0, 3]})
    first = pd.Series([1.0, 1.0, 1.0, 1.0])
    second = pd.Series([np.nan, np.nan, np.nan, 1])
    expected = pd.DataFrame({'first': first, 'second': second})
    with np.errstate(all='ignore'):
        arr = df.values.astype('float') / df.values
    result = pd.DataFrame(arr, index=df.index, columns=df.columns)
    tm.assert_frame_equal(result, expected)