@pytest.mark.parametrize('timestamp, freq, expected', [('20130101 09:10:11', 'D', '20130101'), ('20130101 19:10:11', 'D', '20130102'), ('20130201 12:00:00', 'D', '20130202'), ('20130104 12:00:00', 'D', '20130105'), ('2000-01-05 05:09:15.13', 'D', '2000-01-05 00:00:00'), ('2000-01-05 05:09:15.13', 'H', '2000-01-05 05:00:00'), ('2000-01-05 05:09:15.13', 'S', '2000-01-05 05:09:15')])
def test_round_frequencies(self, timestamp, freq, expected):
    dt = Timestamp(timestamp)
    result = dt.round(freq)
    expected = Timestamp(expected)
    assert result == expected