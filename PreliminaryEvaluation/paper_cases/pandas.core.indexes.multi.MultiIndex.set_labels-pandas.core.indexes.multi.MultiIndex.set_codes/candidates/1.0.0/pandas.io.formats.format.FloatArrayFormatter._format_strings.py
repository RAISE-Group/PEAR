def _format_strings(self) -> List[str]:
    if self.formatter is not None:
        return [self.formatter(x) for x in self.values]
    return list(self.get_result_as_array())