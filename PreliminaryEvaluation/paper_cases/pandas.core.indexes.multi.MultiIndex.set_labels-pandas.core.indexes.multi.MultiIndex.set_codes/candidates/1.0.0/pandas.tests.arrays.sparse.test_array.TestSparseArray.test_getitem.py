def test_getitem(self):

    def _checkit(i):
        tm.assert_almost_equal(self.arr[i], self.arr.to_dense()[i])
    for i in range(len(self.arr)):
        _checkit(i)
        _checkit(-i)