def test_reset_option(self):
    self.cf.register_option('a', 1, 'doc', validator=self.cf.is_int)
    self.cf.register_option('b.c', 'hullo', 'doc2', validator=self.cf.is_str)
    assert self.cf.get_option('a') == 1
    assert self.cf.get_option('b.c') == 'hullo'
    self.cf.set_option('a', 2)
    self.cf.set_option('b.c', 'wurld')
    assert self.cf.get_option('a') == 2
    assert self.cf.get_option('b.c') == 'wurld'
    self.cf.reset_option('a')
    assert self.cf.get_option('a') == 1
    assert self.cf.get_option('b.c') == 'wurld'
    self.cf.reset_option('b.c')
    assert self.cf.get_option('a') == 1
    assert self.cf.get_option('b.c') == 'hullo'