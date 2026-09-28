@pytest.mark.parametrize('op', ['any', 'all'])
def test_logical_compat(self, op):
    index = self.create_index()
    assert getattr(index, op)() == getattr(index.values, op)()