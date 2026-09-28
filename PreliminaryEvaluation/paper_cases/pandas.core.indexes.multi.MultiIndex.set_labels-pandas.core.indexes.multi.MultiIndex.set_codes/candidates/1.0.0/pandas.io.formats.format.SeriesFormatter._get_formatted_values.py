def _get_formatted_values(self) -> List[str]:
    return format_array(self.tr_series._values, None, float_format=self.float_format, na_rep=self.na_rep)