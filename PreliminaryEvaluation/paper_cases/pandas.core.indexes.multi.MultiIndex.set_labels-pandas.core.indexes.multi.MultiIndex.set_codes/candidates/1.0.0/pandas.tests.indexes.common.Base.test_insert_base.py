def test_insert_base(self, indices):
    result = indices[1:4]
    if not len(indices):
        return
    assert indices[0:4].equals(result.insert(0, indices[0]))