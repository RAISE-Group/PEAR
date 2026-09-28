def test_to_pydatetime_nonzero_nano(self):
    ts = Timestamp('2011-01-01 9:00:00.123456789')
    with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
        expected = datetime(2011, 1, 1, 9, 0, 0, 123456)
        result = ts.to_pydatetime()
        assert result == expected