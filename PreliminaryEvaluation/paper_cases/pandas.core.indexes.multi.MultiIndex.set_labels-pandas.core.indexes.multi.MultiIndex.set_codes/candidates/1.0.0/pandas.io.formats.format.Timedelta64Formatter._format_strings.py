def _format_strings(self) -> List[str]:
    formatter = self.formatter or _get_format_timedelta64(self.values, nat_rep=self.nat_rep, box=self.box)
    return [formatter(x) for x in self.values]