def setup_method(self, method):
    super().setup_method(method)
    mask = lambda x: isinstance(x, DatetimeIndex) or isinstance(x, PeriodIndex)
    self.is_valid_objs = [o for o in self.objs if mask(o)]
    self.not_valid_objs = [o for o in self.objs if not mask(o)]