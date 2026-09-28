def test_encode_big_set(self):
    s = set()
    for x in range(0, 100000):
        s.add(x)
    ujson.encode(s)