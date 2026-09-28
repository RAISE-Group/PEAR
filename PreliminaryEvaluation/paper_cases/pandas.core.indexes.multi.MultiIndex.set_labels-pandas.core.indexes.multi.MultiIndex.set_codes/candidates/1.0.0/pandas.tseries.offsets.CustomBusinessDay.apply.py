@apply_wraps
def apply(self, other):
    if self.n <= 0:
        roll = 'forward'
    else:
        roll = 'backward'
    if isinstance(other, datetime):
        date_in = other
        np_dt = np.datetime64(date_in.date())
        np_incr_dt = np.busday_offset(np_dt, self.n, roll=roll, busdaycal=self.calendar)
        dt_date = np_incr_dt.astype(datetime)
        result = datetime.combine(dt_date, date_in.time())
        if self.offset:
            result = result + self.offset
        return result
    elif isinstance(other, (timedelta, Tick)):
        return BDay(self.n, offset=self.offset + other, normalize=self.normalize)
    else:
        raise ApplyTypeError('Only know how to combine trading day with datetime, datetime64 or timedelta.')