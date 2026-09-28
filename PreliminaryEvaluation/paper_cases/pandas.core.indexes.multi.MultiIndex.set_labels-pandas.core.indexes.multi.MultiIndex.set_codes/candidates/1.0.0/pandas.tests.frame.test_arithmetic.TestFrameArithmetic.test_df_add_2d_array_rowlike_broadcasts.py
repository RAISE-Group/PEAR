def test_df_add_2d_array_rowlike_broadcasts(self):
    arr = np.arange(6).reshape(3, 2)
    df = pd.DataFrame(arr, columns=[True, False], index=['A', 'B', 'C'])
    rowlike = arr[[1], :]
    assert rowlike.shape == (1, df.shape[1])
    expected = pd.DataFrame([[2, 4], [4, 6], [6, 8]], columns=df.columns, index=df.index, dtype=arr.dtype)
    result = df + rowlike
    tm.assert_frame_equal(result, expected)
    result = rowlike + df
    tm.assert_frame_equal(result, expected)