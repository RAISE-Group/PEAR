@property
def rule_code(self):
    month = ccalendar.MONTH_ALIASES[self.startingMonth]
    return f'{self._prefix}-{month}'