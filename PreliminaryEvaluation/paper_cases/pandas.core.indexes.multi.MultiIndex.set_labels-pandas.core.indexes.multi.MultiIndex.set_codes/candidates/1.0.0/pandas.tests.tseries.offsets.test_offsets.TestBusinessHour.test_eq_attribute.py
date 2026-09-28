@pytest.mark.parametrize('offset_name', ['offset1', 'offset2', 'offset3', 'offset4', 'offset8', 'offset9', 'offset10'])
def test_eq_attribute(self, offset_name):
    offset = getattr(self, offset_name)
    assert offset == offset