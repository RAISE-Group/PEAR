def test_ceil(self):
    dt = Timestamp('20130101 09:10:11')
    result = dt.ceil('D')
    expected = Timestamp('20130102')
    assert result == expected