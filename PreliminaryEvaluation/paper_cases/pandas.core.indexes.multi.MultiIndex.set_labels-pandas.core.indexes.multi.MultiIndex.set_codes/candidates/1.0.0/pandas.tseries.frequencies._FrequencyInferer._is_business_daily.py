def _is_business_daily(self) -> bool:
    if self.day_deltas != [1, 3]:
        return False
    first_weekday = self.index[0].weekday()
    shifts = np.diff(self.index.asi8)
    shifts = np.floor_divide(shifts, _ONE_DAY)
    weekdays = np.mod(first_weekday + np.cumsum(shifts), 7)
    return np.all((weekdays == 0) & (shifts == 3) | (weekdays > 0) & (weekdays <= 4) & (shifts == 1))