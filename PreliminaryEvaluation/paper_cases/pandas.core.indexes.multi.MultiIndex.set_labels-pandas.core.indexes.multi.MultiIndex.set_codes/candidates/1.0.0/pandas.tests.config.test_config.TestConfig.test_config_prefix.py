def test_config_prefix(self):
    with self.cf.config_prefix('base'):
        self.cf.register_option('a', 1, 'doc1')
        self.cf.register_option('b', 2, 'doc2')
        assert self.cf.get_option('a') == 1
        assert self.cf.get_option('b') == 2
        self.cf.set_option('a', 3)
        self.cf.set_option('b', 4)
        assert self.cf.get_option('a') == 3
        assert self.cf.get_option('b') == 4
    assert self.cf.get_option('base.a') == 3
    assert self.cf.get_option('base.b') == 4
    assert 'doc1' in self.cf.describe_option('base.a', _print_desc=False)
    assert 'doc2' in self.cf.describe_option('base.b', _print_desc=False)
    self.cf.reset_option('base.a')
    self.cf.reset_option('base.b')
    with self.cf.config_prefix('base'):
        assert self.cf.get_option('a') == 1
        assert self.cf.get_option('b') == 2