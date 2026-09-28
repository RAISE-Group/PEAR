def test_slice_keep_name(self):
    idx = RangeIndex(1, 2, name='asdf')
    assert idx.name == idx[1:].name