@pytest.mark.parametrize('indexer_klass', [list, pd.Index])
@pytest.mark.parametrize('indexer', [[True] * 10, [False] * 10, [True, False, True, True, False, False, True, True, False, True]])
def test_bool_indexing(self, indexer_klass, indexer):
    for idx in self.indexes:
        exp_idx = [i for i in range(len(indexer)) if indexer[i]]
        tm.assert_index_equal(idx[indexer_klass(indexer)], idx[exp_idx])
        s = pd.Series(idx)
        tm.assert_series_equal(s[indexer_klass(indexer)], s.iloc[exp_idx])