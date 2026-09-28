def test_sub(self):
    off = self.offset2
    msg = 'Cannot subtract datetime from offset'
    with pytest.raises(TypeError, match=msg):
        off - self.d
    assert 2 * off - off == off
    assert self.d - self.offset2 == self.d + self._offset(-3)