def test_td_rfloordiv_offsets(self):
    assert offsets.Hour(1) // Timedelta(minutes=25) == 2