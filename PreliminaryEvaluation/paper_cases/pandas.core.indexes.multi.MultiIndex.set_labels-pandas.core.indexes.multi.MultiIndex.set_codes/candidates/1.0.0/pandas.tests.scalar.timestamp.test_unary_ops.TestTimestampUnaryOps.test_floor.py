def test_floor(self):
    dt = Timestamp('20130101 09:10:11')
    result = dt.floor('D')
    expected = Timestamp('20130101')
    assert result == expected