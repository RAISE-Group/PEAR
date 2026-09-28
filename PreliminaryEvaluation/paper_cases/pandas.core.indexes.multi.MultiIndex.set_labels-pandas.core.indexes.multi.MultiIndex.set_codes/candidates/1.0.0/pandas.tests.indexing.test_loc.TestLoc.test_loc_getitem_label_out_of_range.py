def test_loc_getitem_label_out_of_range(self):
    self.check_result('loc', 'f', 'loc', 'f', typs=['ints', 'uints', 'labels', 'mixed', 'ts'], fails=KeyError)
    self.check_result('loc', 'f', 'ix', 'f', typs=['floats'], fails=KeyError)
    self.check_result('loc', 'f', 'loc', 'f', typs=['floats'], fails=KeyError)
    self.check_result('loc', 20, 'loc', 20, typs=['ints', 'uints', 'mixed'], fails=KeyError)
    self.check_result('loc', 20, 'loc', 20, typs=['labels'], fails=TypeError)
    self.check_result('loc', 20, 'loc', 20, typs=['ts'], axes=0, fails=TypeError)
    self.check_result('loc', 20, 'loc', 20, typs=['floats'], axes=0, fails=KeyError)