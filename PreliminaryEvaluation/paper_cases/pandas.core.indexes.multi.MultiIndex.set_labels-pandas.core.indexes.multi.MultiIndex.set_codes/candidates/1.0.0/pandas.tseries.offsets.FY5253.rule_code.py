@property
def rule_code(self):
    prefix = self._prefix
    suffix = self.get_rule_code_suffix()
    return f'{prefix}-{suffix}'