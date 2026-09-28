def test_tz_localize_nonexistent_invalid_arg(self):
    tz = 'Europe/Warsaw'
    ts = Timestamp('2015-03-29 02:00:00')
    with pytest.raises(ValueError):
        ts.tz_localize(tz, nonexistent='foo')