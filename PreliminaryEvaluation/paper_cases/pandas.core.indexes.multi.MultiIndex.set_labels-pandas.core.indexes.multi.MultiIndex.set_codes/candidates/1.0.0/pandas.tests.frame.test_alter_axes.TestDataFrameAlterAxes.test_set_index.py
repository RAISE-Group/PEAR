def test_set_index(self, float_string_frame):
    df = float_string_frame
    idx = Index(np.arange(len(df))[::-1])
    df = df.set_index(idx)
    tm.assert_index_equal(df.index, idx)
    with pytest.raises(ValueError, match='Length mismatch'):
        df.set_index(idx[::2])