def get_year_end(self, dt):
    assert dt.tzinfo is None
    dim = ccalendar.get_days_in_month(dt.year, self.startingMonth)
    target_date = datetime(dt.year, self.startingMonth, dim)
    wkday_diff = self.weekday - target_date.weekday()
    if wkday_diff == 0:
        return target_date
    if self.variation == 'last':
        days_forward = wkday_diff % 7 - 7
        return target_date + timedelta(days=days_forward)
    else:
        days_forward = wkday_diff % 7
        if days_forward <= 3:
            return target_date + timedelta(days_forward)
        else:
            return target_date + timedelta(days_forward - 7)