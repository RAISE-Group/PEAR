def test_df_add_2d_array_collike_broadcasts(self):
    arr = np.arange(6).reshape(3, 2)
    df = pd.DataFrame(arr, columns=[True, False], index=['A', 'B', 'C'])
    collike = arr[:, [1]]
    assert collike.shape == (df.shape[0], 1)
    expected = pd.DataFrame([[1, 2], [5, 6], [9, 10]], columns=df.columns, index=df.index, dtype=arr.dtype)
    result = df + collike
    tm.assert_frame_equal(result, expected)
    result = collike + df
    tm.assert_frame_equal(result, expected)