@property
def rule_code(self):
    month = ccalendar.MONTH_ALIASES[self.month]
    return f'{self._prefix}-{month}'