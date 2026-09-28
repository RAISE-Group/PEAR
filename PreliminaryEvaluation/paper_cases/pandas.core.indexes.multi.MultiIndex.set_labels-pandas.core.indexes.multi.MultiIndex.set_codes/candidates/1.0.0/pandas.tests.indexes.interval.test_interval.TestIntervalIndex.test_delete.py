def test_delete(self, closed):
    expected = IntervalIndex.from_breaks(np.arange(1, 11), closed=closed)
    result = self.create_index(closed=closed).delete(0)
    tm.assert_index_equal(result, expected)