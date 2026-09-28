@pytest.mark.xfail(reason='Different repr', strict=True)
def test_array_repr(self, data, size):
    super().test_array_repr(data, size)