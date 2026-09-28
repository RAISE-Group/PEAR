def test_constructor_lists_to_object_dtype(self):
    d = DataFrame({'a': [np.nan, False]})
    assert d['a'].dtype == np.object_
    assert not d['a'][1]