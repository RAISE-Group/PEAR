def test_tricky_container_to_bytes_raises(self):
    msg = "^'str' object cannot be interpreted as an integer$"
    with pytest.raises(TypeError, match=msg):
        bytes(self.unicode_container)