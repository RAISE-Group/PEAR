def test_apply_out_of_range(self, tz_naive_fixture):
    tz = tz_naive_fixture
    if self._offset is None:
        return
    try:
        if self._offset in (BusinessHour, CustomBusinessHour):
            offset = self._get_offset(self._offset, value=100000)
        else:
            offset = self._get_offset(self._offset, value=10000)
        result = Timestamp('20080101') + offset
        assert isinstance(result, datetime)
        assert result.tzinfo is None
        t = Timestamp('20080101', tz=tz)
        result = t + offset
        assert isinstance(result, datetime)
        assert t.tzinfo == result.tzinfo
    except OutOfBoundsDatetime:
        pass
    except (ValueError, KeyError):
        pass