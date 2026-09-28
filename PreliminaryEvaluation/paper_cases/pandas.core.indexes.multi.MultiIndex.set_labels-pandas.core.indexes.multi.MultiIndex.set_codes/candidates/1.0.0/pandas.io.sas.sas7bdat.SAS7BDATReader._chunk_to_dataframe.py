def _chunk_to_dataframe(self):
    n = self._current_row_in_chunk_index
    m = self._current_row_in_file_index
    ix = range(m - n, m)
    rslt = pd.DataFrame(index=ix)
    js, jb = (0, 0)
    for j in range(self.column_count):
        name = self.column_names[j]
        if self._column_types[j] == b'd':
            rslt[name] = self._byte_chunk[jb, :].view(dtype=self.byte_order + 'd')
            rslt[name] = np.asarray(rslt[name], dtype=np.float64)
            if self.convert_dates:
                unit = None
                if self.column_formats[j] in const.sas_date_formats:
                    unit = 'd'
                elif self.column_formats[j] in const.sas_datetime_formats:
                    unit = 's'
                if unit:
                    rslt[name] = pd.to_datetime(rslt[name], unit=unit, origin='1960-01-01')
            jb += 1
        elif self._column_types[j] == b's':
            rslt[name] = self._string_chunk[js, :]
            if self.convert_text and self.encoding is not None:
                rslt[name] = rslt[name].str.decode(self.encoding or self.default_encoding)
            if self.blank_missing:
                ii = rslt[name].str.len() == 0
                rslt.loc[ii, name] = np.nan
            js += 1
        else:
            self.close()
            raise ValueError(f'unknown column type {self._column_types[j]}')
    return rslt