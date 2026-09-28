def test_iadd(self):
    q = r = self.container
    q += [5]
    self.check_result(q, self.lst + [5])
    self.check_result(r, self.lst)