@property
def rule_code(self):
    weekday = ccalendar.int_to_weekday.get(self.weekday, '')
    return f'{self._prefix}-{self.week + 1}{weekday}'