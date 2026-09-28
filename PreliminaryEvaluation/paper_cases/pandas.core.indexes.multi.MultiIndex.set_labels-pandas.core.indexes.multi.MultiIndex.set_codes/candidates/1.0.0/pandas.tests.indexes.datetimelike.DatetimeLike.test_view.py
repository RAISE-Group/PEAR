def test_view(self):
    i = self.create_index()
    i_view = i.view('i8')
    result = self._holder(i)
    tm.assert_index_equal(result, i)
    i_view = i.view(self._holder)
    result = self._holder(i)
    tm.assert_index_equal(result, i_view)