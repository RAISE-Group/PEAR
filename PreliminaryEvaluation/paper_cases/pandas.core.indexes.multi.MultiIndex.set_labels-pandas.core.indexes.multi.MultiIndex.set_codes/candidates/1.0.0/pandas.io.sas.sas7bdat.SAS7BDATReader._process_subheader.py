def _process_subheader(self, subheader_index, pointer):
    offset = pointer.offset
    length = pointer.length
    if subheader_index == const.SASIndex.row_size_index:
        processor = self._process_rowsize_subheader
    elif subheader_index == const.SASIndex.column_size_index:
        processor = self._process_columnsize_subheader
    elif subheader_index == const.SASIndex.column_text_index:
        processor = self._process_columntext_subheader
    elif subheader_index == const.SASIndex.column_name_index:
        processor = self._process_columnname_subheader
    elif subheader_index == const.SASIndex.column_attributes_index:
        processor = self._process_columnattributes_subheader
    elif subheader_index == const.SASIndex.format_and_label_index:
        processor = self._process_format_subheader
    elif subheader_index == const.SASIndex.column_list_index:
        processor = self._process_columnlist_subheader
    elif subheader_index == const.SASIndex.subheader_counts_index:
        processor = self._process_subheader_counts
    elif subheader_index == const.SASIndex.data_subheader_index:
        self._current_page_data_subheader_pointers.append(pointer)
        return
    else:
        raise ValueError('unknown subheader index')
    processor(offset, length)