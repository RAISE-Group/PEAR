def test_join_self(self, join_type):
    index = self.create_index()
    joined = index.join(index, how=join_type)
    assert index is joined