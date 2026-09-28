def test_swapaxes(self):
    df = DataFrame(np.random.randn(10, 5))
    tm.assert_frame_equal(df.T, df.swapaxes(0, 1))
    tm.assert_frame_equal(df.T, df.swapaxes(1, 0))
    tm.assert_frame_equal(df, df.swapaxes(0, 0))
    msg = "No axis named 2 for object type <class 'pandas.core(.sparse)?.frame.(Sparse)?DataFrame'>"
    with pytest.raises(ValueError, match=msg):
        df.swapaxes(2, 5)