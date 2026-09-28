def test_is_on_offset(self, offset_types):
    dt = self.expecteds[offset_types.__name__]
    offset_s = self._get_offset(offset_types)
    assert offset_s.is_on_offset(dt)
    if issubclass(offset_types, Tick):
        return
    offset_n = self._get_offset(offset_types, normalize=True)
    assert not offset_n.is_on_offset(dt)
    if offset_types in (BusinessHour, CustomBusinessHour):
        return
    date = datetime(dt.year, dt.month, dt.day)
    assert offset_n.is_on_offset(date)