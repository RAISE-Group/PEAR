def _read_subheader_signature(self, offset):
    subheader_signature = self._read_bytes(offset, self._int_length)
    return subheader_signature