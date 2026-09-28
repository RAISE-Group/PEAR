@pytest.mark.parametrize('idx,nm,prop', [(pd.Index([1]), 'index', 'name'), (pd.Index([1], name='myname'), 'myname', 'name'), (pd.MultiIndex.from_product([('a', 'b'), ('c', 'd')]), ['level_0', 'level_1'], 'names'), (pd.MultiIndex.from_product([('a', 'b'), ('c', 'd')], names=['n1', 'n2']), ['n1', 'n2'], 'names'), (pd.MultiIndex.from_product([('a', 'b'), ('c', 'd')], names=['n1', None]), ['n1', 'level_1'], 'names')])
def test_set_names_unset(self, idx, nm, prop):
    data = pd.Series(1, idx)
    result = set_default_names(data)
    assert getattr(result.index, prop) == nm