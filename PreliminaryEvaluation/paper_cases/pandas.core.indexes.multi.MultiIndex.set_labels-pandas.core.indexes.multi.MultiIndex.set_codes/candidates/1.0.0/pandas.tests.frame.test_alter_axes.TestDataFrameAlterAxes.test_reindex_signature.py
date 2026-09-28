def test_reindex_signature(self):
    sig = inspect.signature(DataFrame.reindex)
    parameters = set(sig.parameters)
    assert parameters == {'self', 'labels', 'index', 'columns', 'axis', 'limit', 'copy', 'level', 'method', 'fill_value', 'tolerance'}