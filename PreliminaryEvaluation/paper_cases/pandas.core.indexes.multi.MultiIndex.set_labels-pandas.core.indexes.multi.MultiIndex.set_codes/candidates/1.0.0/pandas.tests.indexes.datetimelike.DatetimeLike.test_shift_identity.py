def test_shift_identity(self):
    idx = self.create_index()
    tm.assert_index_equal(idx, idx.shift(0))