def teardown_method(self, method):
    del self.lhses, self.rhses, self.scalar_rhses, self.scalar_lhses
    del self.pandas_rhses, self.pandas_lhses, self.current_engines