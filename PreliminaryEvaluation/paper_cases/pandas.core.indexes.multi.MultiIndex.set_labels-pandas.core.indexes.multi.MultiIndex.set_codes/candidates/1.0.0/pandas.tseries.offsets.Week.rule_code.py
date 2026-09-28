@property
def rule_code(self):
    suffix = ''
    if self.weekday is not None:
        weekday = ccalendar.int_to_weekday[self.weekday]
        suffix = f'-{weekday}'
    return self._prefix + suffix