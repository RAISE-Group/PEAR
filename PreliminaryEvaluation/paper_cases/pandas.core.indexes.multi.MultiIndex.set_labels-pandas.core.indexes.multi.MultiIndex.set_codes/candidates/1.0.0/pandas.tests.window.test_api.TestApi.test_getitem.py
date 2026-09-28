def test_getitem(self):
    r = self.frame.rolling(window=5)
    tm.assert_index_equal(r._selected_obj.columns, self.frame.columns)
    r = self.frame.rolling(window=5)[1]
    assert r._selected_obj.name == self.frame.columns[1]
    r = self.frame.rolling(window=5)[1, 3]
    tm.assert_index_equal(r._selected_obj.columns, self.frame.columns[[1, 3]])
    r = self.frame.rolling(window=5)[[1, 3]]
    tm.assert_index_equal(r._selected_obj.columns, self.frame.columns[[1, 3]])