def _process_subheader_pointers(self, offset, subheader_pointer_index):
    subheader_pointer_length = self._subheader_pointer_length
    total_offset = offset + subheader_pointer_length * subheader_pointer_index
    subheader_offset = self._read_int(total_offset, self._int_length)
    total_offset += self._int_length
    subheader_length = self._read_int(total_offset, self._int_length)
    total_offset += self._int_length
    subheader_compression = self._read_int(total_offset, 1)
    total_offset += 1
    subheader_type = self._read_int(total_offset, 1)
    x = _subheader_pointer()
    x.offset = subheader_offset
    x.length = subheader_length
    x.compression = subheader_compression
    x.ptype = subheader_type
    return x