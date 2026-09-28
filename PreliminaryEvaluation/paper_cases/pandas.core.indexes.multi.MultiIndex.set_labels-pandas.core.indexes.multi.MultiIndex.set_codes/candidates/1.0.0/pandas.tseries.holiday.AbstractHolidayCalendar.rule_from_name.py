def rule_from_name(self, name):
    for rule in self.rules:
        if rule.name == name:
            return rule
    return None