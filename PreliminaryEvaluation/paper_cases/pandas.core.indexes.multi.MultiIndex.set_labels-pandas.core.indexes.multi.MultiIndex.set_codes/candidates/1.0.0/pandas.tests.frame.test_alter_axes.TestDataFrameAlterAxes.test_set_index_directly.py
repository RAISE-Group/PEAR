def test_set_index_directly(self, float_string_frame):
    df = float_string_frame
    idx = Index(np.arange(len(df))[::-1])
    df.index = idx
    tm.assert_index_equal(df.index, idx)
    with pytest.raises(ValueError, match='Length mismatch'):
        df.index = idx[::2]