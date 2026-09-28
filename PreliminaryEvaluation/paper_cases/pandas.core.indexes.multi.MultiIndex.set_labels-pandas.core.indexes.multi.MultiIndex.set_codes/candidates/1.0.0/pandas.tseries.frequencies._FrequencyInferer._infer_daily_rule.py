def _infer_daily_rule(self) -> Optional[str]:
    annual_rule = self._get_annual_rule()
    if annual_rule:
        nyears = self.ydiffs[0]
        month = MONTH_ALIASES[self.rep_stamp.month]
        alias = f'{annual_rule}-{month}'
        return _maybe_add_count(alias, nyears)
    quarterly_rule = self._get_quarterly_rule()
    if quarterly_rule:
        nquarters = self.mdiffs[0] / 3
        mod_dict = {0: 12, 2: 11, 1: 10}
        month = MONTH_ALIASES[mod_dict[self.rep_stamp.month % 3]]
        alias = f'{quarterly_rule}-{month}'
        return _maybe_add_count(alias, nquarters)
    monthly_rule = self._get_monthly_rule()
    if monthly_rule:
        return _maybe_add_count(monthly_rule, self.mdiffs[0])
    if self.is_unique:
        days = self.deltas[0] / _ONE_DAY
        if days % 7 == 0:
            day = int_to_weekday[self.rep_stamp.weekday()]
            return _maybe_add_count(f'W-{day}', days / 7)
        else:
            return _maybe_add_count('D', days)
    if self._is_business_daily():
        return 'B'
    wom_rule = self._get_wom_rule()
    if wom_rule:
        return wom_rule
    return None