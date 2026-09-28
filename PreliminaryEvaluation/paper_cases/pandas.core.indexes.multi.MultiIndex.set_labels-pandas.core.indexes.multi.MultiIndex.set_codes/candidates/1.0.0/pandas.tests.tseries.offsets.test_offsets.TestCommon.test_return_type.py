def test_return_type(self, offset_types):
    offset = self._get_offset(offset_types)
    result = Timestamp('20080101') + offset
    assert isinstance(result, Timestamp)
    assert NaT + offset is NaT
    assert offset + NaT is NaT
    assert NaT - offset is NaT
    assert (-offset).apply(NaT) is NaT