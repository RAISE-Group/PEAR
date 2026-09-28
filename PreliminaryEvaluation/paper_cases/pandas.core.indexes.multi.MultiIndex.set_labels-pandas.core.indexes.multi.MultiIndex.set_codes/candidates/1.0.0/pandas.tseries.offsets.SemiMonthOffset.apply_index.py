@apply_index_wraps
def apply_index(self, i):
    dti = i
    days_from_start = i.to_perioddelta('M').asi8
    delta = Timedelta(days=self.day_of_month - 1).value
    before_day_of_month = days_from_start < delta
    after_day_of_month = days_from_start > delta
    roll = self._get_roll(i, before_day_of_month, after_day_of_month)
    time = i.to_perioddelta('D')
    asper = i.to_period('M')
    if not isinstance(asper._data, np.ndarray):
        asper = asper._data
    shifted = asper._addsub_int_array(roll // 2, operator.add)
    i = type(dti)(shifted.to_timestamp())
    i = self._apply_index_days(i, roll)
    return i + time