def test_hash(self):
    assert hash(self.offset1) == hash(self.offset1)
    assert hash(self.offset2) == hash(self.offset2)