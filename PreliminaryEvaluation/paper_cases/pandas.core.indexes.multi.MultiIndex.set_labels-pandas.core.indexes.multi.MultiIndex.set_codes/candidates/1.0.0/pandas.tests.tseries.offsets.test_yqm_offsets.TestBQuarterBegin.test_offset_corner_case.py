def test_offset_corner_case(self):
    offset = BQuarterBegin(n=-1, startingMonth=1)
    assert datetime(2007, 4, 3) + offset == datetime(2007, 4, 2)