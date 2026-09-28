def setup_method(self, method):
    self.regular = DataFrame({'A': date_range('20130101', periods=5, freq='s'), 'B': range(5)}).set_index('A')
    self.ragged = DataFrame({'B': range(5)})
    self.ragged.index = [Timestamp('20130101 09:00:00'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:05'), Timestamp('20130101 09:00:06')]