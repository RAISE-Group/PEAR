def get_rule_code_suffix(self):
    prefix = self._get_suffix_prefix()
    month = ccalendar.MONTH_ALIASES[self.startingMonth]
    weekday = ccalendar.int_to_weekday[self.weekday]
    return f'{prefix}-{month}-{weekday}'