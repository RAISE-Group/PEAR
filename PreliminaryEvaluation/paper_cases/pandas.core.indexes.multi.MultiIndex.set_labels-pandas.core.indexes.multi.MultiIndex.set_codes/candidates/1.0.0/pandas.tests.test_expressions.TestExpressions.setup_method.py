def setup_method(self, method):
    self.frame = _frame.copy()
    self.frame2 = _frame2.copy()
    self.mixed = _mixed.copy()
    self.mixed2 = _mixed2.copy()
    self._MIN_ELEMENTS = expr._MIN_ELEMENTS