@property
def rule_code(self):
    suffix = f'-{self.day_of_month}'
    return self._prefix + suffix