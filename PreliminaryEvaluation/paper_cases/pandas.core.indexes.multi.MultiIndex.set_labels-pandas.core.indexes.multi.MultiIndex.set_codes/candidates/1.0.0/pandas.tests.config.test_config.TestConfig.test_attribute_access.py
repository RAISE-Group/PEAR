def test_attribute_access(self):
    holder = []

    def f3(key):
        holder.append(True)
    self.cf.register_option('a', 0)
    self.cf.register_option('c', 0, cb=f3)
    options = self.cf.options
    assert options.a == 0
    with self.cf.option_context('a', 15):
        assert options.a == 15
    options.a = 500
    assert self.cf.get_option('a') == 500
    self.cf.reset_option('a')
    assert options.a == self.cf.get_option('a', 0)
    msg = 'You can only set the value of existing options'
    with pytest.raises(OptionError, match=msg):
        options.b = 1
    with pytest.raises(OptionError, match=msg):
        options.display = 1
    options.c = 1
    assert len(holder) == 1