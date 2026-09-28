def test_dti_tz_localize_roundtrip(self, tz_aware_fixture):
    idx = date_range(start='2014-06-01', end='2014-08-30', freq='15T')
    tz = tz_aware_fixture
    localized = idx.tz_localize(tz)
    with pytest.raises(TypeError):
        localized.tz_localize(tz)
    reset = localized.tz_localize(None)
    assert reset.tzinfo is None
    tm.assert_index_equal(reset, idx)