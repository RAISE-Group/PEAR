def test_reindex_no_type_preserve_target_empty_mi(self):
    index = pd.Index(list('abc'))
    result = index.reindex(pd.MultiIndex([pd.Int64Index([]), pd.Float64Index([])], [[], []]))[0]
    assert result.levels[0].dtype.type == np.int64
    assert result.levels[1].dtype.type == np.float64