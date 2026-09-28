def test_nonunique_contains(self):
    for idx in map(DatetimeIndex, ([0, 1, 0], [0, 0, -1], [0, -1, -1], ['2015', '2015', '2016'], ['2015', '2015', '2014'])):
        assert idx[0] in idx