def _write_col_header(self, indent: int) -> None:
    truncate_h = self.fmt.truncate_h
    if isinstance(self.columns, ABCMultiIndex):
        template = 'colspan="{span:d}" halign="left"'
        if self.fmt.sparsify:
            sentinel = lib.no_default
        else:
            sentinel = False
        levels = self.columns.format(sparsify=sentinel, adjoin=False, names=False)
        level_lengths = get_level_lengths(levels, sentinel)
        inner_lvl = len(level_lengths) - 1
        for lnum, (records, values) in enumerate(zip(level_lengths, levels)):
            if truncate_h:
                ins_col = self.fmt.tr_col_num
                if self.fmt.sparsify:
                    recs_new = {}
                    for tag, span in list(records.items()):
                        if tag >= ins_col:
                            recs_new[tag + 1] = span
                        elif tag + span > ins_col:
                            recs_new[tag] = span + 1
                            if lnum == inner_lvl:
                                values = values[:ins_col] + ('...',) + values[ins_col:]
                            else:
                                values = values[:ins_col] + (values[ins_col - 1],) + values[ins_col:]
                        else:
                            recs_new[tag] = span
                        if tag + span == ins_col:
                            recs_new[ins_col] = 1
                            values = values[:ins_col] + ('...',) + values[ins_col:]
                    records = recs_new
                    inner_lvl = len(level_lengths) - 1
                    if lnum == inner_lvl:
                        records[ins_col] = 1
                else:
                    recs_new = {}
                    for tag, span in list(records.items()):
                        if tag >= ins_col:
                            recs_new[tag + 1] = span
                        else:
                            recs_new[tag] = span
                    recs_new[ins_col] = 1
                    records = recs_new
                    values = values[:ins_col] + ['...'] + values[ins_col:]
            row = [''] * (self.row_levels - 1)
            if self.fmt.index or self.show_col_idx_names:
                if self.fmt.show_index_names:
                    name = self.columns.names[lnum]
                    row.append(pprint_thing(name or ''))
                else:
                    row.append('')
            tags = {}
            j = len(row)
            for i, v in enumerate(values):
                if i in records:
                    if records[i] > 1:
                        tags[j] = template.format(span=records[i])
                else:
                    continue
                j += 1
                row.append(v)
            self.write_tr(row, indent, self.indent_delta, tags=tags, header=True)
    else:
        row = [''] * (self.row_levels - 1)
        if self.fmt.index or self.show_col_idx_names:
            if self.fmt.show_index_names:
                row.append(self.columns.name or '')
            else:
                row.append('')
        row.extend(self._get_columns_formatted_values())
        align = self.fmt.justify
        if truncate_h:
            ins_col = self.row_levels + self.fmt.tr_col_num
            row.insert(ins_col, '...')
        self.write_tr(row, indent, self.indent_delta, header=True, align=align)