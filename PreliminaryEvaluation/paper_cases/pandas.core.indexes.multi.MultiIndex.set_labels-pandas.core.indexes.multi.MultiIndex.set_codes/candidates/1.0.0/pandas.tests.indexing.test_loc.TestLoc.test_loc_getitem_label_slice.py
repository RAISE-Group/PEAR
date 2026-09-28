def test_loc_getitem_label_slice(self):
    self.check_result('loc', slice(1, 3), 'loc', slice(1, 3), typs=['labels', 'mixed', 'empty', 'ts', 'floats'], fails=TypeError)
    self.check_result('loc', slice('20130102', '20130104'), 'loc', slice('20130102', '20130104'), typs=['ts'], axes=1, fails=TypeError)
    self.check_result('loc', slice(2, 8), 'loc', slice(2, 8), typs=['mixed'], axes=0, fails=TypeError)
    self.check_result('loc', slice(2, 8), 'loc', slice(2, 8), typs=['mixed'], axes=1, fails=KeyError)
    self.check_result('loc', slice(2, 4, 2), 'loc', slice(2, 4, 2), typs=['mixed'], axes=0, fails=TypeError)