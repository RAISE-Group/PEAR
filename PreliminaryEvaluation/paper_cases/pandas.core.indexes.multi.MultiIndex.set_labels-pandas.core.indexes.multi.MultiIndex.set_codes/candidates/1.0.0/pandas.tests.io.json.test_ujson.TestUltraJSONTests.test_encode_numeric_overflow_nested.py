def test_encode_numeric_overflow_nested(self):

    class Nested:
        x = 12839128391289382193812939
    for _ in range(0, 100):
        with pytest.raises(OverflowError):
            ujson.encode(Nested())