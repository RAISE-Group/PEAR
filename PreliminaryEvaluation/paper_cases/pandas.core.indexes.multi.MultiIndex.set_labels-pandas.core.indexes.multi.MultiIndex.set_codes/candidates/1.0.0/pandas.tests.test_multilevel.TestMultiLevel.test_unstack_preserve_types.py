def test_unstack_preserve_types(self):
    self.ymd['E'] = 'foo'
    self.ymd['F'] = 2
    unstacked = self.ymd.unstack('month')
    assert unstacked['A', 1].dtype == np.float64
    assert unstacked['E', 1].dtype == np.object_
    assert unstacked['F', 1].dtype == np.float64