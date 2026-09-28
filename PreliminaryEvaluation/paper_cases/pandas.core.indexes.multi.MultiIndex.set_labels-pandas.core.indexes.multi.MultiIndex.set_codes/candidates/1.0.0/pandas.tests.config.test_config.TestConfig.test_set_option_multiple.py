def test_set_option_multiple(self):
    self.cf.register_option('a', 1, 'doc')
    self.cf.register_option('b.c', 'hullo', 'doc2')
    self.cf.register_option('b.b', None, 'doc2')
    assert self.cf.get_option('a') == 1
    assert self.cf.get_option('b.c') == 'hullo'
    assert self.cf.get_option('b.b') is None
    self.cf.set_option('a', '2', 'b.c', None, 'b.b', 10.0)
    assert self.cf.get_option('a') == '2'
    assert self.cf.get_option('b.c') is None
    assert self.cf.get_option('b.b') == 10.0