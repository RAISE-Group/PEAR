def test_tz_localize_ambiguous_bool(self):
    ts = Timestamp('2015-11-01 01:00:03')
    expected0 = Timestamp('2015-11-01 01:00:03-0500', tz='US/Central')
    expected1 = Timestamp('2015-11-01 01:00:03-0600', tz='US/Central')
    with pytest.raises(pytz.AmbiguousTimeError):
        ts.tz_localize('US/Central')
    result = ts.tz_localize('US/Central', ambiguous=True)
    assert result == expected0
    result = ts.tz_localize('US/Central', ambiguous=False)
    assert result == expected1