def test_repr_roundtrip(self):
    index = self.create_index()
    tm.assert_index_equal(eval(repr(index)), index)