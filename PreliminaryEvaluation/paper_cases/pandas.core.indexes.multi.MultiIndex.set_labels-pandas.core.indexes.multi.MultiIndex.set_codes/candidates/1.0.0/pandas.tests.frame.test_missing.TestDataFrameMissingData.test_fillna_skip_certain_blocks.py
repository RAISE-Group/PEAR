def test_fillna_skip_certain_blocks(self):
    df = DataFrame(np.random.randn(10, 4).astype(int))
    df.fillna(np.nan)