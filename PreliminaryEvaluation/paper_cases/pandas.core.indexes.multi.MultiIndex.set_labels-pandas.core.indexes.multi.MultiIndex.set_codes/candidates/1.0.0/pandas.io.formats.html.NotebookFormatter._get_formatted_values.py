def _get_formatted_values(self) -> Dict[int, List[str]]:
    return {i: self.fmt._format_col(i) for i in range(self.ncols)}