def test_loc_getitem_label_list_with_missing(self):
    self.check_result('loc', [0, 1, 2], 'loc', [0, 1, 2], typs=['empty'], fails=KeyError)
    self.check_result('loc', [0, 2, 10], 'ix', [0, 2, 10], typs=['ints', 'uints', 'floats'], axes=0, fails=KeyError)
    self.check_result('loc', [3, 6, 7], 'ix', [3, 6, 7], typs=['ints', 'uints', 'floats'], axes=1, fails=KeyError)
    self.check_result('loc', [(1, 3), (1, 4), (2, 5)], 'ix', [(1, 3), (1, 4), (2, 5)], typs=['multi'], axes=0, fails=KeyError)