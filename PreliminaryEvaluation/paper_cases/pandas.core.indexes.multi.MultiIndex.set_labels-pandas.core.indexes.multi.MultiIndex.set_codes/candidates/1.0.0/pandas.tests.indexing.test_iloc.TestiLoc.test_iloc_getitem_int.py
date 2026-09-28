def test_iloc_getitem_int(self):
    self.check_result('iloc', 2, 'iloc', 2, typs=['labels', 'mixed', 'ts', 'floats', 'empty'], fails=IndexError)