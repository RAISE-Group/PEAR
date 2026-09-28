@property
def rule_code(self):
    suffix = self._offset.get_rule_code_suffix()
    qtr = self.qtr_with_extra_week
    return f'{self._prefix}-{suffix}-{qtr}'