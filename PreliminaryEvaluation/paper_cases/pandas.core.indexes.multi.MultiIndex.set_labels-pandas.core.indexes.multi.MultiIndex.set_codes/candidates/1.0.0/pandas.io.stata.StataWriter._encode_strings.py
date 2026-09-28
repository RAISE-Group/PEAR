def _encode_strings(self):
    """
        Encode strings in dta-specific encoding

        Do not encode columns marked for date conversion or for strL
        conversion. The strL converter independently handles conversion and
        also accepts empty string arrays.
        """
    convert_dates = self._convert_dates
    convert_strl = getattr(self, '_convert_strl', [])
    for i, col in enumerate(self.data):
        if i in convert_dates or col in convert_strl:
            continue
        column = self.data[col]
        dtype = column.dtype
        if dtype.type == np.object_:
            inferred_dtype = infer_dtype(column, skipna=True)
            if not (inferred_dtype in ('string', 'unicode') or len(column) == 0):
                col = column.name
                raise ValueError(f'Column `{col}` cannot be exported.\n\nOnly string-like object arrays\ncontaining all strings or a mix of strings and None can be exported.\nObject arrays containing only null values are prohibited. Other object\ntypes cannot be exported and must first be converted to one of the\nsupported types.')
            encoded = self.data[col].str.encode(self._encoding)
            if max_len_string_array(ensure_object(encoded.values)) <= self._max_string_length:
                self.data[col] = encoded