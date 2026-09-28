def test_onOffset_deprecated(self, offset_types):
    off = self._get_offset(offset_types)
    ts = Timestamp.now()
    with tm.assert_produces_warning(FutureWarning):
        result = off.onOffset(ts)
    expected = off.is_on_offset(ts)
    assert result == expected