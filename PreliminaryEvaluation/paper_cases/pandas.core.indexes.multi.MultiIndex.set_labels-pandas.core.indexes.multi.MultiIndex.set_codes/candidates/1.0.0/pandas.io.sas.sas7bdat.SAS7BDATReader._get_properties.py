def _get_properties(self):
    self._path_or_buf.seek(0)
    self._cached_page = self._path_or_buf.read(288)
    if self._cached_page[0:len(const.magic)] != const.magic:
        self.close()
        raise ValueError('magic number mismatch (not a SAS file?)')
    align1, align2 = (0, 0)
    buf = self._read_bytes(const.align_1_offset, const.align_1_length)
    if buf == const.u64_byte_checker_value:
        align2 = const.align_2_value
        self.U64 = True
        self._int_length = 8
        self._page_bit_offset = const.page_bit_offset_x64
        self._subheader_pointer_length = const.subheader_pointer_length_x64
    else:
        self.U64 = False
        self._page_bit_offset = const.page_bit_offset_x86
        self._subheader_pointer_length = const.subheader_pointer_length_x86
        self._int_length = 4
    buf = self._read_bytes(const.align_2_offset, const.align_2_length)
    if buf == const.align_1_checker_value:
        align1 = const.align_2_value
    total_align = align1 + align2
    buf = self._read_bytes(const.endianness_offset, const.endianness_length)
    if buf == b'\x01':
        self.byte_order = '<'
    else:
        self.byte_order = '>'
    buf = self._read_bytes(const.encoding_offset, const.encoding_length)[0]
    if buf in const.encoding_names:
        self.file_encoding = const.encoding_names[buf]
    else:
        self.file_encoding = f'unknown (code={buf})'
    buf = self._read_bytes(const.platform_offset, const.platform_length)
    if buf == b'1':
        self.platform = 'unix'
    elif buf == b'2':
        self.platform = 'windows'
    else:
        self.platform = 'unknown'
    buf = self._read_bytes(const.dataset_offset, const.dataset_length)
    self.name = buf.rstrip(b'\x00 ')
    if self.convert_header_text:
        self.name = self.name.decode(self.encoding or self.default_encoding)
    buf = self._read_bytes(const.file_type_offset, const.file_type_length)
    self.file_type = buf.rstrip(b'\x00 ')
    if self.convert_header_text:
        self.file_type = self.file_type.decode(self.encoding or self.default_encoding)
    epoch = datetime(1960, 1, 1)
    x = self._read_float(const.date_created_offset + align1, const.date_created_length)
    self.date_created = epoch + pd.to_timedelta(x, unit='s')
    x = self._read_float(const.date_modified_offset + align1, const.date_modified_length)
    self.date_modified = epoch + pd.to_timedelta(x, unit='s')
    self.header_length = self._read_int(const.header_size_offset + align1, const.header_size_length)
    buf = self._path_or_buf.read(self.header_length - 288)
    self._cached_page += buf
    if len(self._cached_page) != self.header_length:
        self.close()
        raise ValueError('The SAS7BDAT file appears to be truncated.')
    self._page_length = self._read_int(const.page_size_offset + align1, const.page_size_length)
    self._page_count = self._read_int(const.page_count_offset + align1, const.page_count_length)
    buf = self._read_bytes(const.sas_release_offset + total_align, const.sas_release_length)
    self.sas_release = buf.rstrip(b'\x00 ')
    if self.convert_header_text:
        self.sas_release = self.sas_release.decode(self.encoding or self.default_encoding)
    buf = self._read_bytes(const.sas_server_type_offset + total_align, const.sas_server_type_length)
    self.server_type = buf.rstrip(b'\x00 ')
    if self.convert_header_text:
        self.server_type = self.server_type.decode(self.encoding or self.default_encoding)
    buf = self._read_bytes(const.os_version_number_offset + total_align, const.os_version_number_length)
    self.os_version = buf.rstrip(b'\x00 ')
    if self.convert_header_text:
        self.os_version = self.os_version.decode(self.encoding or self.default_encoding)
    buf = self._read_bytes(const.os_name_offset + total_align, const.os_name_length)
    buf = buf.rstrip(b'\x00 ')
    if len(buf) > 0:
        self.os_name = buf.decode(self.encoding or self.default_encoding)
    else:
        buf = self._read_bytes(const.os_maker_offset + total_align, const.os_maker_length)
        self.os_name = buf.rstrip(b'\x00 ')
        if self.convert_header_text:
            self.os_name = self.os_name.decode(self.encoding or self.default_encoding)