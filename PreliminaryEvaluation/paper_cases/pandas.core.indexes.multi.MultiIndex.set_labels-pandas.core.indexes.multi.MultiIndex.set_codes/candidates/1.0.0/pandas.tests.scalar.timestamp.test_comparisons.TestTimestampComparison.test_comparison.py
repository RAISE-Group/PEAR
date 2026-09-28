def test_comparison(self):
    stamp = 1337299200000000000
    val = Timestamp(stamp)
    assert val == val
    assert not val != val
    assert not val < val
    assert val <= val
    assert not val > val
    assert val >= val
    other = datetime(2012, 5, 18)
    assert val == other
    assert not val != other
    assert not val < other
    assert val <= other
    assert not val > other
    assert val >= other
    other = Timestamp(stamp + 100)
    assert val != other
    assert val != other
    assert val < other
    assert val <= other
    assert other > val
    assert other >= val