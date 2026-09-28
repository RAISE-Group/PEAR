def test_get_option(self):
    self.cf.register_option('a', 1, 'doc')
    self.cf.register_option('b.c', 'hullo', 'doc2')
    self.cf.register_option('b.b', None, 'doc2')
    assert self.cf.get_option('a') == 1
    assert self.cf.get_option('b.c') == 'hullo'
    assert self.cf.get_option('b.b') is None
    msg = "No such keys\\(s\\): 'no_such_option'"
    with pytest.raises(OptionError, match=msg):
        self.cf.get_option('no_such_option')