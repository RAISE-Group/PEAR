def test_no_values_attribute(self, data):
    assert not hasattr(data, 'values')
    assert not hasattr(data, '_values')