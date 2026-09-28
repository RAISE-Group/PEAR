def setup_method(self, method):
    self.d = datetime(2014, 7, 1, 10, 0)
    self.offset1 = CustomBusinessHour(weekmask='Tue Wed Thu Fri')
    self.offset2 = CustomBusinessHour(holidays=self.holidays)