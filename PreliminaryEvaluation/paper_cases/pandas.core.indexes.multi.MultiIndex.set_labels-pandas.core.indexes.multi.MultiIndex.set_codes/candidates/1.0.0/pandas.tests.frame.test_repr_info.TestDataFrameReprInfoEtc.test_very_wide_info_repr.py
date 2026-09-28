def test_very_wide_info_repr(self):
    df = DataFrame(np.random.randn(10, 20), columns=tm.rands_array(10, 20))
    repr(df)