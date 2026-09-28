def test_option_context_scope(self):
    original_value = 60
    context_value = 10
    option_name = 'a'
    self.cf.register_option(option_name, original_value)
    ctx = self.cf.option_context(option_name, context_value)
    assert self.cf.get_option(option_name) == original_value
    with ctx:
        assert self.cf.get_option(option_name) == context_value
    assert self.cf.get_option(option_name) == original_value