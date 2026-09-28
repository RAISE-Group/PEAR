def _format_strings(self) -> List[str]:
    formatter = self.formatter or (lambda x: '{x: d}'.format(x=x))
    fmt_values = [formatter(x) for x in self.values]
    return fmt_values