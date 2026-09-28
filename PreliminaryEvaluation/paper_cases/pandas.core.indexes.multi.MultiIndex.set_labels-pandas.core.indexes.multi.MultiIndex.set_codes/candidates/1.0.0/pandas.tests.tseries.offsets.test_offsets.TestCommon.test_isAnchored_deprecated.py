def test_isAnchored_deprecated(self, offset_types):
    off = self._get_offset(offset_types)
    with tm.assert_produces_warning(FutureWarning):
        result = off.isAnchored()
    expected = off.is_anchored()
    assert result == expected