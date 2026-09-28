def test_indexing_doesnt_change_class(self):
    index = Index([1, 2, 3, 'a', 'b', 'c'])
    assert index[1:3].identical(pd.Index([2, 3], dtype=np.object_))
    assert index[[0, 1]].identical(pd.Index([1, 2], dtype=np.object_))