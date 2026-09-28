def test_td_floordiv_offsets(self):
    td = Timedelta(hours=3, minutes=4)
    assert td // offsets.Hour(1) == 3
    assert td // offsets.Minute(2) == 92