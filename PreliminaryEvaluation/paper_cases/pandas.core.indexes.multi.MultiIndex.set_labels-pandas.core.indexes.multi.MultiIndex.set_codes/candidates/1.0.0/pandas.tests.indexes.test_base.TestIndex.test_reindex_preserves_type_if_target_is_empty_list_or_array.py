@pytest.mark.parametrize('labels', [[], np.array([]), np.array([], dtype=np.int64)])
def test_reindex_preserves_type_if_target_is_empty_list_or_array(self, labels):
    index = pd.Index(list('abc'))
    assert index.reindex(labels)[0].dtype.type == np.object_