def test_combine_first(self, data):
    if data.dtype.subtype == 'int':
        pytest.skip('TODO(SparseArray.__setitem__ will preserve dtype.')
    super().test_combine_first(data)