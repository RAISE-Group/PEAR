def test_to_dict(self):
    d = {'key': 31337}

    class DictTest:

        def toDict(self):
            return d
    o = DictTest()
    output = ujson.encode(o)
    dec = ujson.decode(output)
    assert dec == d