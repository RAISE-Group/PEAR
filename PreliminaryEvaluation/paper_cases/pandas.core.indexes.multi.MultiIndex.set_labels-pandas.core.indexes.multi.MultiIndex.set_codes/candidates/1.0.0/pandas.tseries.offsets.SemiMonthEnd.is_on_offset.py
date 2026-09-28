def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    days_in_month = ccalendar.get_days_in_month(dt.year, dt.month)
    return dt.day in (self.day_of_month, days_in_month)