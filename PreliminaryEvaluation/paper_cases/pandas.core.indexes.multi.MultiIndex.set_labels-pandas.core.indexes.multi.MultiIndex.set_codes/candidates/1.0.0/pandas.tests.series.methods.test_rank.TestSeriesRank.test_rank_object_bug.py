def test_rank_object_bug(self):
    Series([np.nan] * 32).astype(object).rank(ascending=True)
    Series([np.nan] * 32).astype(object).rank(ascending=False)