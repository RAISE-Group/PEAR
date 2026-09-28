def test_compare_str(self):
    if self._offset is None:
        return
    off = self._get_offset(self._offset)
    assert not off == 'infer'
    assert off != 'foo'