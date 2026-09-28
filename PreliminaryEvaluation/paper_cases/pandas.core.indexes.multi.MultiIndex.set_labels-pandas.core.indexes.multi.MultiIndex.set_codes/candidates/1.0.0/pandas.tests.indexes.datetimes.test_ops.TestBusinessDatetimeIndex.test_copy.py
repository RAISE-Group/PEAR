def test_copy(self):
    cp = self.rng.copy()
    repr(cp)
    tm.assert_index_equal(cp, self.rng)