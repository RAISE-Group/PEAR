def test_loc_getitem_label_list_fails(self):
    self.check_result('loc', [20, 30, 40], 'loc', [20, 30, 40], typs=['ints', 'uints'], axes=1, fails=KeyError)