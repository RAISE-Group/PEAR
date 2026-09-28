def setup_method(self, method):
    self.pc = converter.PeriodConverter()

    class Axis:
        pass
    self.axis = Axis()
    self.axis.freq = 'D'