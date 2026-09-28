def test_validation(self):
    self.cf.register_option('a', 1, 'doc', validator=self.cf.is_int)
    self.cf.register_option('d', 1, 'doc', validator=self.cf.is_nonnegative_int)
    self.cf.register_option('b.c', 'hullo', 'doc2', validator=self.cf.is_text)
    msg = "Value must have type '<class 'int'>'"
    with pytest.raises(ValueError, match=msg):
        self.cf.register_option('a.b.c.d2', 'NO', 'doc', validator=self.cf.is_int)
    self.cf.set_option('a', 2)
    self.cf.set_option('b.c', 'wurld')
    self.cf.set_option('d', 2)
    self.cf.set_option('d', None)
    with pytest.raises(ValueError, match=msg):
        self.cf.set_option('a', None)
    with pytest.raises(ValueError, match=msg):
        self.cf.set_option('a', 'ab')
    msg = 'Value must be a nonnegative integer or None'
    with pytest.raises(ValueError, match=msg):
        self.cf.register_option('a.b.c.d3', 'NO', 'doc', validator=self.cf.is_nonnegative_int)
    with pytest.raises(ValueError, match=msg):
        self.cf.register_option('a.b.c.d3', -2, 'doc', validator=self.cf.is_nonnegative_int)
    msg = "Value must be an instance of <class 'str'>\\|<class 'bytes'>"
    with pytest.raises(ValueError, match=msg):
        self.cf.set_option('b.c', 1)
    validator = self.cf.is_one_of_factory([None, self.cf.is_callable])
    self.cf.register_option('b', lambda: None, 'doc', validator=validator)
    self.cf.set_option('b', '%.1f'.format)
    self.cf.set_option('b', None)
    with pytest.raises(ValueError, match='Value must be a callable'):
        self.cf.set_option('b', '%.1f')