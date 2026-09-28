def _process_page_metadata(self):
    bit_offset = self._page_bit_offset
    for i in range(self._current_page_subheaders_count):
        pointer = self._process_subheader_pointers(const.subheader_pointers_offset + bit_offset, i)
        if pointer.length == 0:
            continue
        if pointer.compression == const.truncated_subheader_id:
            continue
        subheader_signature = self._read_subheader_signature(pointer.offset)
        subheader_index = self._get_subheader_index(subheader_signature, pointer.compression, pointer.ptype)
        self._process_subheader(subheader_index, pointer)