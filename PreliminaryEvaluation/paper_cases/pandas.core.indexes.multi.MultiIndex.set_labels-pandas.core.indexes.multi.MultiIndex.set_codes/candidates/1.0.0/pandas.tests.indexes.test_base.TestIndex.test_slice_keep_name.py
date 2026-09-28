def test_slice_keep_name(self):
    index = Index(['a', 'b'], name='asdf')
    assert index.name == index[1:].name