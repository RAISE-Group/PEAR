def test_str_to_bytes_raises(self):
    index = Index([str(x) for x in range(10)])
    msg = "^'str' object cannot be interpreted as an integer$"
    with pytest.raises(TypeError, match=msg):
        bytes(index)