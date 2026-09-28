def year_has_extra_week(self, dt):
    norm = Timestamp(dt).normalize().tz_localize(None)
    next_year_end = self._offset.rollforward(norm)
    prev_year_end = norm - self._offset
    weeks_in_year = (next_year_end - prev_year_end).days / 7
    assert weeks_in_year in [52, 53], weeks_in_year
    return weeks_in_year == 53