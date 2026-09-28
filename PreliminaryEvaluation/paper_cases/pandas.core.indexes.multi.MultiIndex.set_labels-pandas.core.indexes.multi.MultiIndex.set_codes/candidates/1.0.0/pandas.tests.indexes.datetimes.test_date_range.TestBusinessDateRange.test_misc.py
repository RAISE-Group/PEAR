def test_misc(self):
    end = datetime(2009, 5, 13)
    dr = bdate_range(end=end, periods=20)
    firstDate = end - 19 * BDay()
    assert len(dr) == 20
    assert dr[0] == firstDate
    assert dr[-1] == end