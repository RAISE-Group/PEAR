def generate_value_label(self, byteorder):
    """
        Generate the binary representation of the value labals.

        Parameters
        ----------
        byteorder : str
            Byte order of the output

        Returns
        -------
        value_label : bytes
            Bytes containing the formatted value label
        """
    encoding = self._encoding
    bio = BytesIO()
    null_byte = b'\x00'
    bio.write(struct.pack(byteorder + 'i', self.len))
    labname = self.labname[:32].encode(encoding)
    lab_len = 32 if encoding not in ('utf-8', 'utf8') else 128
    labname = _pad_bytes(labname, lab_len + 1)
    bio.write(labname)
    for i in range(3):
        bio.write(struct.pack('c', null_byte))
    bio.write(struct.pack(byteorder + 'i', self.n))
    bio.write(struct.pack(byteorder + 'i', self.text_len))
    for offset in self.off:
        bio.write(struct.pack(byteorder + 'i', offset))
    for value in self.val:
        bio.write(struct.pack(byteorder + 'i', value))
    for text in self.txt:
        bio.write(text + null_byte)
    bio.seek(0)
    return bio.read()