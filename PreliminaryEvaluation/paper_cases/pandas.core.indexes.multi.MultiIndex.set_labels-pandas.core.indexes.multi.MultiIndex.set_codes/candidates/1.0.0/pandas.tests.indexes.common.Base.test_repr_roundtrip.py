def test_repr_roundtrip(self):
    idx = self.create_index()
    tm.assert_index_equal(eval(repr(idx)), idx)