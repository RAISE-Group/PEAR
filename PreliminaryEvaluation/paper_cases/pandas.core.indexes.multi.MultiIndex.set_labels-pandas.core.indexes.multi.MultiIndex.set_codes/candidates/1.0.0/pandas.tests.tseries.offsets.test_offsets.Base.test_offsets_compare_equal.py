def test_offsets_compare_equal(self):
    if self._offset is None:
        return
    offset1 = self._offset()
    offset2 = self._offset()
    assert not offset1 != offset2
    assert offset1 == offset2