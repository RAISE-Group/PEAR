def test_encode_numeric_overflow(self):
    with pytest.raises(OverflowError):
        ujson.encode(12839128391289382193812939)