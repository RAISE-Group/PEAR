def test_round_30min(self):
    dt = Timestamp('20130104 12:32:00')
    result = dt.round('30Min')
    expected = Timestamp('20130104 12:30:00')
    assert result == expected