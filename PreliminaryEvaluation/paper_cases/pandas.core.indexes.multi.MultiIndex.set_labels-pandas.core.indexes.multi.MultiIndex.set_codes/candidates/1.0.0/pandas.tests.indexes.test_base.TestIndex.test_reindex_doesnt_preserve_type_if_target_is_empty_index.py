@pytest.mark.parametrize('labels,dtype', [(pd.Int64Index([]), np.int64), (pd.Float64Index([]), np.float64), (pd.DatetimeIndex([]), np.datetime64)])
def test_reindex_doesnt_preserve_type_if_target_is_empty_index(self, labels, dtype):
    index = pd.Index(list('abc'))
    assert index.reindex(labels)[0].dtype.type == dtype