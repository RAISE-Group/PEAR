def test_nbytes(self):
    i = RangeIndex(0, 1000)
    assert i.nbytes < i._int64index.nbytes / 10
    i2 = RangeIndex(0, 10)
    assert i.nbytes == i2.nbytes