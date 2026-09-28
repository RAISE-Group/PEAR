def test_integer_passthrough(self):
    rs = self.pc.convert([0, 1], None, self.axis)
    xp = [0, 1]
    assert rs == xp