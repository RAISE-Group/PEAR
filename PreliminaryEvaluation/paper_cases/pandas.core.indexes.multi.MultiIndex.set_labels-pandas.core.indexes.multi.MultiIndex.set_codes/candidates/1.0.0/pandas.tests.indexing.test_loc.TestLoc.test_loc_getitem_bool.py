def test_loc_getitem_bool(self):
    b = [True, False, True, False]
    self.check_result('loc', b, 'loc', b, typs=['empty'], fails=IndexError)