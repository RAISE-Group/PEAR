@pytest.mark.parametrize('name', [None, 'foobar'])
@pytest.mark.parametrize('labels', [[], np.array([]), ['A', 'B', 'C'], ['C', 'B', 'A'], np.array(['A', 'B', 'C']), np.array(['C', 'B', 'A']), pd.date_range('20130101', periods=3).values, pd.date_range('20130101', periods=3).tolist()])
def test_reindex_preserves_name_if_target_is_list_or_ndarray(self, name, labels):
    index = pd.Index([0, 1, 2])
    index.name = name
    assert index.reindex(labels)[0].name == name