def test_setitem_fancy_scalar(self, float_frame):
    f = float_frame
    expected = float_frame.copy()
    ix = f.loc
    for j, col in enumerate(f.columns):
        ts = f[col]
        for idx in f.index[::5]:
            i = f.index.get_loc(idx)
            val = np.random.randn()
            expected.values[i, j] = val
            ix[idx, col] = val
            tm.assert_frame_equal(f, expected)