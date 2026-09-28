def _get_formatted_values(self) -> Dict[int, List[str]]:
    with option_context('display.max_colwidth', None):
        fmt_values = {i: self.fmt._format_col(i) for i in range(self.ncols)}
    return fmt_values