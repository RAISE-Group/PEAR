def get_weeks(self, dt):
    ret = [13] * 4
    year_has_extra_week = self.year_has_extra_week(dt)
    if year_has_extra_week:
        ret[self.qtr_with_extra_week - 1] = 14
    return ret