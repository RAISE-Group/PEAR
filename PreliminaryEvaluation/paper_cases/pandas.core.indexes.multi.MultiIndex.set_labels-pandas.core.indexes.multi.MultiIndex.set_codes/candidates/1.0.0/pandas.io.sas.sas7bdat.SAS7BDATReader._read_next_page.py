def _read_next_page(self):
    self._current_page_data_subheader_pointers = []
    self._cached_page = self._path_or_buf.read(self._page_length)
    if len(self._cached_page) <= 0:
        return True
    elif len(self._cached_page) != self._page_length:
        self.close()
        msg = f'failed to read complete page from file (read {len(self._cached_page):d} of {self._page_length:d} bytes)'
        raise ValueError(msg)
    self._read_page_header()
    page_type = self._current_page_type
    if page_type == const.page_meta_type:
        self._process_page_metadata()
    is_data_page = page_type & const.page_data_type
    pt = [const.page_meta_type] + const.page_mix_types
    if not is_data_page and self._current_page_type not in pt:
        return self._read_next_page()
    return False