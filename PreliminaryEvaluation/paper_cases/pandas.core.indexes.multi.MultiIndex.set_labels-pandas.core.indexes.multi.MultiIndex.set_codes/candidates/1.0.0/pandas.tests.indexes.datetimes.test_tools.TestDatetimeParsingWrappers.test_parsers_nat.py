def test_parsers_nat(self):
    result1, _, _ = parsing.parse_time_string('NaT')
    result2 = to_datetime('NaT')
    result3 = Timestamp('NaT')
    result4 = DatetimeIndex(['NaT'])[0]
    assert result1 is NaT
    assert result2 is NaT
    assert result3 is NaT
    assert result4 is NaT