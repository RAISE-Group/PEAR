@property
def name(self):
    if self.is_anchored:
        return self.rule_code
    else:
        month = ccalendar.MONTH_ALIASES[self.n]
        return f'{self.code_rule}-{month}'