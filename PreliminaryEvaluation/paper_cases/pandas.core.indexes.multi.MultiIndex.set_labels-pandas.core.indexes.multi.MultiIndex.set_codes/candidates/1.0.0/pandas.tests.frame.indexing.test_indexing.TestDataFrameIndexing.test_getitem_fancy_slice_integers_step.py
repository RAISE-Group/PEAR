def test_getitem_fancy_slice_integers_step(self):
    df = DataFrame(np.random.randn(10, 5))
    result = df.iloc[:8:2]
    df.iloc[:8:2] = np.nan
    assert isna(df.iloc[:8:2]).values.all()