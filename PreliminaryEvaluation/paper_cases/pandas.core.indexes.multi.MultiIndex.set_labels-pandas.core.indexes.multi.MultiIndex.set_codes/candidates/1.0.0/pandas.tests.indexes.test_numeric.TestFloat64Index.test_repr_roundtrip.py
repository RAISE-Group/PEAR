def test_repr_roundtrip(self, indices):
    tm.assert_index_equal(eval(repr(indices)), indices)