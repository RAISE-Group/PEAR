def teardown_method(self, method):
    setattr(self.cf, '_global_config', self.gc)
    setattr(self.cf, '_deprecated_options', self.do)
    setattr(self.cf, '_registered_options', self.ro)