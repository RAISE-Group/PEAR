def test_convert_nested(self):
    data = ['2012-1-1', '2012-1-2']
    r1 = self.pc.convert([data, data], None, self.axis)
    r2 = [self.pc.convert(data, None, self.axis) for _ in range(2)]
    assert r1 == r2