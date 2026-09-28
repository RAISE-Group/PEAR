def test_immutable(self, offset_types):
    offset = self._get_offset(offset_types)
    with pytest.raises(AttributeError):
        offset.normalize = True
    with pytest.raises(AttributeError):
        offset.n = 91