def test_offset_corner_case(self):
    offset = BQuarterEnd(n=-1, startingMonth=1)
    assert datetime(2010, 1, 31) + offset == datetime(2010, 1, 29)