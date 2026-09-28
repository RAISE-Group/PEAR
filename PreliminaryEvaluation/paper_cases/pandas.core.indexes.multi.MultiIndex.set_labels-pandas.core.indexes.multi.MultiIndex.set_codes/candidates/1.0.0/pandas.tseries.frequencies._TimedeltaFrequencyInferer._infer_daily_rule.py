def _infer_daily_rule(self):
    if self.is_unique:
        days = self.deltas[0] / _ONE_DAY
        if days % 7 == 0:
            wd = int_to_weekday[self.rep_stamp.weekday()]
            alias = f'W-{wd}'
            return _maybe_add_count(alias, days / 7)
        else:
            return _maybe_add_count('D', days)