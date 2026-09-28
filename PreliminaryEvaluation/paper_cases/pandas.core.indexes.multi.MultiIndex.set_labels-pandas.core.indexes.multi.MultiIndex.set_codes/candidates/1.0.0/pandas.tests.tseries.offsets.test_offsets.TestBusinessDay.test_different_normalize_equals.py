def test_different_normalize_equals(self):
    offset = self._offset()
    offset2 = self._offset(normalize=True)
    assert offset != offset2