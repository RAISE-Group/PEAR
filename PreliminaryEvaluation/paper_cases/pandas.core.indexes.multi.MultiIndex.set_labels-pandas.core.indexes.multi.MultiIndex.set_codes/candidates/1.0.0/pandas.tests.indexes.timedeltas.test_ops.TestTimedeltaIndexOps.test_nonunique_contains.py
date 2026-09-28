def test_nonunique_contains(self):
    for idx in map(TimedeltaIndex, ([0, 1, 0], [0, 0, -1], [0, -1, -1], ['00:01:00', '00:01:00', '00:02:00'], ['00:01:00', '00:01:00', '00:00:01'])):
        assert idx[0] in idx