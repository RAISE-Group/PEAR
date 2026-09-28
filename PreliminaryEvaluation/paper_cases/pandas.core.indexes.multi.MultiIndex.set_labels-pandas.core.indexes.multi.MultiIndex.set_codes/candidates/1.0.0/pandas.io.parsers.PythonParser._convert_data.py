def _convert_data(self, data):

    def _clean_mapping(mapping):
        """converts col numbers to names"""
        clean = {}
        for col, v in mapping.items():
            if isinstance(col, int) and col not in self.orig_names:
                col = self.orig_names[col]
            clean[col] = v
        return clean
    clean_conv = _clean_mapping(self.converters)
    if not isinstance(self.dtype, dict):
        clean_dtypes = self.dtype
    else:
        clean_dtypes = _clean_mapping(self.dtype)
    clean_na_values = {}
    clean_na_fvalues = {}
    if isinstance(self.na_values, dict):
        for col in self.na_values:
            na_value = self.na_values[col]
            na_fvalue = self.na_fvalues[col]
            if isinstance(col, int) and col not in self.orig_names:
                col = self.orig_names[col]
            clean_na_values[col] = na_value
            clean_na_fvalues[col] = na_fvalue
    else:
        clean_na_values = self.na_values
        clean_na_fvalues = self.na_fvalues
    return self._convert_to_ndarrays(data, clean_na_values, clean_na_fvalues, self.verbose, clean_conv, clean_dtypes)