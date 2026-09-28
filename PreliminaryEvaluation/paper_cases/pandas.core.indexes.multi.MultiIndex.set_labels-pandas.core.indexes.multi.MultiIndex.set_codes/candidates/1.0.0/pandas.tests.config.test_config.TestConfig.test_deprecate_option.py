def test_deprecate_option(self):
    self.cf.deprecate_option('foo')
    assert self.cf._is_deprecated('foo')
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        with pytest.raises(KeyError, match="No such keys.s.: 'foo'"):
            self.cf.get_option('foo')
        assert len(w) == 1
        assert 'deprecated' in str(w[-1])
    self.cf.register_option('a', 1, 'doc', validator=self.cf.is_int)
    self.cf.register_option('b.c', 'hullo', 'doc2')
    self.cf.register_option('foo', 'hullo', 'doc2')
    self.cf.deprecate_option('a', removal_ver='nifty_ver')
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        self.cf.get_option('a')
        assert len(w) == 1
        assert 'eprecated' in str(w[-1])
        assert 'nifty_ver' in str(w[-1])
        msg = "Option 'a' has already been defined as deprecated"
        with pytest.raises(OptionError, match=msg):
            self.cf.deprecate_option('a')
    self.cf.deprecate_option('b.c', 'zounds!')
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        self.cf.get_option('b.c')
        assert len(w) == 1
        assert 'zounds!' in str(w[-1])
    self.cf.register_option('d.a', 'foo', 'doc2')
    self.cf.register_option('d.dep', 'bar', 'doc2')
    assert self.cf.get_option('d.a') == 'foo'
    assert self.cf.get_option('d.dep') == 'bar'
    self.cf.deprecate_option('d.dep', rkey='d.a')
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        assert self.cf.get_option('d.dep') == 'foo'
        assert len(w) == 1
        assert 'eprecated' in str(w[-1])
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        self.cf.set_option('d.dep', 'baz')
        assert len(w) == 1
        assert 'eprecated' in str(w[-1])
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        assert self.cf.get_option('d.dep') == 'baz'
        assert len(w) == 1
        assert 'eprecated' in str(w[-1])