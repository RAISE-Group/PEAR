def is_on_offset(self, dt):
    if self.normalize and (not _is_normalized(dt)):
        return False
    dt = datetime(dt.year, dt.month, dt.day)
    year_end = self.get_year_end(dt)
    if self.variation == 'nearest':
        return year_end == dt or self.get_year_end(shift_month(dt, -1, None)) == dt
    else:
        return year_end == dt