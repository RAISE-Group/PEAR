def test_iloc_getitem_neg_int(self):
    self.check_result('iloc', -1, 'iloc', -1, typs=['labels', 'mixed', 'ts', 'floats', 'empty'], fails=IndexError)