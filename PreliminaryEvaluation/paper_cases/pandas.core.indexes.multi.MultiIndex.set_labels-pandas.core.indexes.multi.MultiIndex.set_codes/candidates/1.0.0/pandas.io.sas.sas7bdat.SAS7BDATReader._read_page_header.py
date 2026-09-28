def _read_page_header(self):
    bit_offset = self._page_bit_offset
    tx = const.page_type_offset + bit_offset
    self._current_page_type = self._read_int(tx, const.page_type_length)
    tx = const.block_count_offset + bit_offset
    self._current_page_block_count = self._read_int(tx, const.block_count_length)
    tx = const.subheader_count_offset + bit_offset
    self._current_page_subheaders_count = self._read_int(tx, const.subheader_count_length)