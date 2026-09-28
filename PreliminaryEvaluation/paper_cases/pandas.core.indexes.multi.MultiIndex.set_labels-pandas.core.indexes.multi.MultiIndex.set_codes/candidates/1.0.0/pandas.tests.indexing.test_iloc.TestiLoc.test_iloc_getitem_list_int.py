def test_iloc_getitem_list_int(self):
    self.check_result('iloc', [0, 1, 2], 'iloc', [0, 1, 2], typs=['labels', 'mixed', 'ts', 'floats', 'empty'], fails=IndexError)