def test_loc_getitem_int(self):
    self.check_result('loc', 2, 'loc', 2, typs=['label'], fails=KeyError)