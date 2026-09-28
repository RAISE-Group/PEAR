def setup_method(self, method):
    super().setup_method(method)
    self.is_valid_objs = self.objs
    self.not_valid_objs = []