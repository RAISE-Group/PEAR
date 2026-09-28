def test_set_option(self):
    self.cf.register_option('a', 1, 'doc')
    self.cf.register_option('b.c', 'hullo', 'doc2')
    self.cf.register_option('b.b', None, 'doc2')
    assert self.cf.get_option('a') == 1
    assert self.cf.get_option('b.c') == 'hullo'
    assert self.cf.get_option('b.b') is None
    self.cf.set_option('a', 2)
    self.cf.set_option('b.c', 'wurld')
    self.cf.set_option('b.b', 1.1)
    assert self.cf.get_option('a') == 2
    assert self.cf.get_option('b.c') == 'wurld'
    assert self.cf.get_option('b.b') == 1.1
    msg = "No such keys\\(s\\): 'no.such.key'"
    with pytest.raises(OptionError, match=msg):
        self.cf.set_option('no.such.key', None)