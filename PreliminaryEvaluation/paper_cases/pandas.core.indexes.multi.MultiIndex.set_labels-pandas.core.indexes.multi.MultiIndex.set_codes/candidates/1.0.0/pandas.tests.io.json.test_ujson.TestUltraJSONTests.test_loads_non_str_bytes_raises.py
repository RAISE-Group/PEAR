def test_loads_non_str_bytes_raises(self):
    msg = "Expected 'str' or 'bytes'"
    with pytest.raises(TypeError, match=msg):
        ujson.loads(None)