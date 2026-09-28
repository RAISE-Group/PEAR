def test_intersection_bug_1708(self):
    from pandas import DateOffset
    index_1 = date_range('1/1/2012', periods=4, freq='12H')
    index_2 = index_1 + DateOffset(hours=1)
    result = index_1 & index_2
    assert len(result) == 0