def test_hash_equivalent(self):
    d = {datetime(2011, 1, 1): 5}
    stamp = Timestamp(datetime(2011, 1, 1))
    assert d[stamp] == 5