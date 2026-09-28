def test_str_to_bytes_raises(self):
    df = Series(['abc'], name='abc')
    msg = "^'str' object cannot be interpreted as an integer$"
    with pytest.raises(TypeError, match=msg):
        bytes(df)