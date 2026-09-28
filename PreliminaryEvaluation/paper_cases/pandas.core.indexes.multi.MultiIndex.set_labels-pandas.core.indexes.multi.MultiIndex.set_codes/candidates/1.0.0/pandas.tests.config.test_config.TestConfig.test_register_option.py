def test_register_option(self):
    self.cf.register_option('a', 1, 'doc')
    msg = "Option 'a' has already been registered"
    with pytest.raises(OptionError, match=msg):
        self.cf.register_option('a', 1, 'doc')
    msg = "Path prefix to option 'a' is already an option"
    with pytest.raises(OptionError, match=msg):
        self.cf.register_option('a.b.c.d1', 1, 'doc')
    with pytest.raises(OptionError, match=msg):
        self.cf.register_option('a.b.c.d2', 1, 'doc')
    msg = 'for is a python keyword'
    with pytest.raises(ValueError, match=msg):
        self.cf.register_option('for', 0)
    with pytest.raises(ValueError, match=msg):
        self.cf.register_option('a.for.b', 0)
    msg = 'oh my goddess! is not a valid identifier'
    with pytest.raises(ValueError, match=msg):
        self.cf.register_option('Oh my Goddess!', 0)
    self.cf.register_option('k.b.c.d1', 1, 'doc')
    self.cf.register_option('k.b.c.d2', 1, 'doc')