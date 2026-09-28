def test_tz_localize_ambiguous_raise(self):
    ts = Timestamp('2015-11-1 01:00')
    with pytest.raises(AmbiguousTimeError):
        ts.tz_localize('US/Pacific', ambiguous='raise')