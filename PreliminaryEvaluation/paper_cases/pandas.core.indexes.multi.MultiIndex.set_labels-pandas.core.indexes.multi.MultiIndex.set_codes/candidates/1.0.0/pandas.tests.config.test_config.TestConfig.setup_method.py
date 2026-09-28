def setup_method(self, method):
    setattr(self.cf, '_global_config', {})
    setattr(self.cf, 'options', self.cf.DictWrapper(self.cf._global_config))
    setattr(self.cf, '_deprecated_options', {})
    setattr(self.cf, '_registered_options', {})
    self.cf.register_option('chained_assignment', 'raise')