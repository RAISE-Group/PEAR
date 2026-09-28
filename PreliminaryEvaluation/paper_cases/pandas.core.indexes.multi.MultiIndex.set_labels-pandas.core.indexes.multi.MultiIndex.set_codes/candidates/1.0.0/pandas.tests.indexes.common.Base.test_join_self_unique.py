def test_join_self_unique(self, join_type):
    index = self.create_index()
    if index.is_unique:
        joined = index.join(index, how=join_type)
        assert (index == joined).all()