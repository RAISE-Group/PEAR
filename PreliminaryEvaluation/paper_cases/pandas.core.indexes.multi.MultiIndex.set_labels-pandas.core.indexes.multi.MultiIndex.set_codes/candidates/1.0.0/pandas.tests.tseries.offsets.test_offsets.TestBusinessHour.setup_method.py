def setup_method(self, method):
    self.d = datetime(2014, 7, 1, 10, 0)
    self.offset1 = BusinessHour()
    self.offset2 = BusinessHour(n=3)
    self.offset3 = BusinessHour(n=-1)
    self.offset4 = BusinessHour(n=-4)
    from datetime import time as dt_time
    self.offset5 = BusinessHour(start=dt_time(11, 0), end=dt_time(14, 30))
    self.offset6 = BusinessHour(start='20:00', end='05:00')
    self.offset7 = BusinessHour(n=-2, start=dt_time(21, 30), end=dt_time(6, 30))
    self.offset8 = BusinessHour(start=['09:00', '13:00'], end=['12:00', '17:00'])
    self.offset9 = BusinessHour(n=3, start=['09:00', '22:00'], end=['13:00', '03:00'])
    self.offset10 = BusinessHour(n=-1, start=['23:00', '13:00'], end=['02:00', '17:00'])