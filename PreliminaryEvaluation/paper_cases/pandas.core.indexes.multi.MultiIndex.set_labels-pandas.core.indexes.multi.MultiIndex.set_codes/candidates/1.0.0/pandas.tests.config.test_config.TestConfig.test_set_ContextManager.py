def test_set_ContextManager(self):

    def eq(val):
        assert self.cf.get_option('a') == val
    self.cf.register_option('a', 0)
    eq(0)
    with self.cf.option_context('a', 15):
        eq(15)
        with self.cf.option_context('a', 25):
            eq(25)
        eq(15)
    eq(0)
    self.cf.set_option('a', 17)
    eq(17)