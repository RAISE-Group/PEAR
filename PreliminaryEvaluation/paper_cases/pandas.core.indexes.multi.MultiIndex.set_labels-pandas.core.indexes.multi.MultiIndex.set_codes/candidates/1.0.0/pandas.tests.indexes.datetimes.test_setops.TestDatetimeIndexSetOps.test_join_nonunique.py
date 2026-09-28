def test_join_nonunique(self):
    idx1 = to_datetime(['2012-11-06 16:00:11.477563', '2012-11-06 16:00:11.477563'])
    idx2 = to_datetime(['2012-11-06 15:11:09.006507', '2012-11-06 15:11:09.006507'])
    rs = idx1.join(idx2, how='outer')
    assert rs.is_monotonic