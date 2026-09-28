def setup_method(self, method):
    self.setup_ops()
    self.setup_data()
    self.current_engines = filter(lambda x: x != self.engine, _engines)