def test_getitem_fancy_scalar(self, float_frame):
    f = float_frame
    ix = f.loc
    for col in f.columns:
        ts = f[col]
        for idx in f.index[::5]:
            assert ix[idx, col] == ts[idx]