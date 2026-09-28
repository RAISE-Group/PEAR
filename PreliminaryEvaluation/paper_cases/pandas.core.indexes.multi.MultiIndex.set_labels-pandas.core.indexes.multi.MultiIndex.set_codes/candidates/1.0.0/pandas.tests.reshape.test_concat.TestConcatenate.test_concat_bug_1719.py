def test_concat_bug_1719(self):
    ts1 = tm.makeTimeSeries()
    ts2 = tm.makeTimeSeries()[::2]
    left = concat([ts1, ts2], join='outer', axis=1)
    right = concat([ts2, ts1], join='outer', axis=1)
    assert len(left) == len(right)