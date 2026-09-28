def test_loc_getitem_label(self):
    self.check_result('loc', 'c', 'loc', 'c', typs=['empty'], fails=KeyError)