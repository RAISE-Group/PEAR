def test_unicode_repr_issues(self):
    levels = [Index(['a/σ', 'b/σ', 'c/σ']), Index([0, 1])]
    codes = [np.arange(3).repeat(2), np.tile(np.arange(2), 3)]
    index = MultiIndex(levels=levels, codes=codes)
    repr(index.levels)