def _process_columnname_subheader(self, offset, length):
    int_len = self._int_length
    offset += int_len
    column_name_pointers_count = (length - 2 * int_len - 12) // 8
    for i in range(column_name_pointers_count):
        text_subheader = offset + const.column_name_pointer_length * (i + 1) + const.column_name_text_subheader_offset
        col_name_offset = offset + const.column_name_pointer_length * (i + 1) + const.column_name_offset_offset
        col_name_length = offset + const.column_name_pointer_length * (i + 1) + const.column_name_length_offset
        idx = self._read_int(text_subheader, const.column_name_text_subheader_length)
        col_offset = self._read_int(col_name_offset, const.column_name_offset_length)
        col_len = self._read_int(col_name_length, const.column_name_length_length)
        name_str = self.column_names_strings[idx]
        self.column_names.append(name_str[col_offset:col_offset + col_len])