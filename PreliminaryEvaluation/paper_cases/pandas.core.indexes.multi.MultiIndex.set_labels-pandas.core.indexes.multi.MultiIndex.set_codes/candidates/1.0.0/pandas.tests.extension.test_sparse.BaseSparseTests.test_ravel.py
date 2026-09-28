@pytest.mark.xfail(reason='SparseArray does not support setitem')
def test_ravel(self, data):
    super().test_ravel(data)