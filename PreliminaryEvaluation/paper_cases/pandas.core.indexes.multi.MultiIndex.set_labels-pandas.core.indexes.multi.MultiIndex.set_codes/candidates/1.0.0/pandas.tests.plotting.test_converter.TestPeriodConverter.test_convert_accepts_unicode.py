def test_convert_accepts_unicode(self):
    r1 = self.pc.convert('2012-1-1', None, self.axis)
    r2 = self.pc.convert('2012-1-1', None, self.axis)
    assert r1 == r2