def test_from_2d_ndarray_with_dtype(self):
    array_dim2 = np.arange(10).reshape((5, 2))
    df = pd.DataFrame(array_dim2, dtype='datetime64[ns, UTC]')
    expected = pd.DataFrame(array_dim2).astype('datetime64[ns, UTC]')
    tm.assert_frame_equal(df, expected)