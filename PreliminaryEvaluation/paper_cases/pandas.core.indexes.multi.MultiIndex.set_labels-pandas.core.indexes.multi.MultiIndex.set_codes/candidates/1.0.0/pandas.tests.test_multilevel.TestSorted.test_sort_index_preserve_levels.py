def test_sort_index_preserve_levels(self):
    result = self.frame.sort_index()
    assert result.index.names == self.frame.index.names