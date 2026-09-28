def _translate(self):
    """
        Convert the DataFrame in `self.data` and the attrs from `_build_styles`
        into a dictionary of {head, body, uuid, cellstyle}.
        """
    table_styles = self.table_styles or []
    caption = self.caption
    ctx = self.ctx
    precision = self.precision
    hidden_index = self.hidden_index
    hidden_columns = self.hidden_columns
    uuid = self.uuid or str(uuid1()).replace('-', '_')
    ROW_HEADING_CLASS = 'row_heading'
    COL_HEADING_CLASS = 'col_heading'
    INDEX_NAME_CLASS = 'index_name'
    DATA_CLASS = 'data'
    BLANK_CLASS = 'blank'
    BLANK_VALUE = ''

    def format_attr(pair):
        return f"{pair['key']}={pair['value']}"
    idx_lengths = _get_level_lengths(self.index)
    col_lengths = _get_level_lengths(self.columns, hidden_columns)
    cell_context = dict()
    n_rlvls = self.data.index.nlevels
    n_clvls = self.data.columns.nlevels
    rlabels = self.data.index.tolist()
    clabels = self.data.columns.tolist()
    if n_rlvls == 1:
        rlabels = [[x] for x in rlabels]
    if n_clvls == 1:
        clabels = [[x] for x in clabels]
    clabels = list(zip(*clabels))
    cellstyle = []
    head = []
    for r in range(n_clvls):
        row_es = [{'type': 'th', 'value': BLANK_VALUE, 'display_value': BLANK_VALUE, 'is_visible': not hidden_index, 'class': ' '.join([BLANK_CLASS])}] * (n_rlvls - 1)
        name = self.data.columns.names[r]
        cs = [BLANK_CLASS if name is None else INDEX_NAME_CLASS, f'level{r}']
        name = BLANK_VALUE if name is None else name
        row_es.append({'type': 'th', 'value': name, 'display_value': name, 'class': ' '.join(cs), 'is_visible': not hidden_index})
        if clabels:
            for c, value in enumerate(clabels[r]):
                cs = [COL_HEADING_CLASS, f'level{r}', f'col{c}']
                cs.extend(cell_context.get('col_headings', {}).get(r, {}).get(c, []))
                es = {'type': 'th', 'value': value, 'display_value': value, 'class': ' '.join(cs), 'is_visible': _is_visible(c, r, col_lengths)}
                colspan = col_lengths.get((r, c), 0)
                if colspan > 1:
                    es['attributes'] = [format_attr({'key': 'colspan', 'value': colspan})]
                row_es.append(es)
            head.append(row_es)
    if self.data.index.names and com.any_not_none(*self.data.index.names) and (not hidden_index):
        index_header_row = []
        for c, name in enumerate(self.data.index.names):
            cs = [INDEX_NAME_CLASS, f'level{c}']
            name = '' if name is None else name
            index_header_row.append({'type': 'th', 'value': name, 'class': ' '.join(cs)})
        index_header_row.extend([{'type': 'th', 'value': BLANK_VALUE, 'class': ' '.join([BLANK_CLASS])}] * (len(clabels[0]) - len(hidden_columns)))
        head.append(index_header_row)
    body = []
    for r, idx in enumerate(self.data.index):
        row_es = []
        for c, value in enumerate(rlabels[r]):
            rid = [ROW_HEADING_CLASS, f'level{c}', f'row{r}']
            es = {'type': 'th', 'is_visible': _is_visible(r, c, idx_lengths) and (not hidden_index), 'value': value, 'display_value': value, 'id': '_'.join(rid[1:]), 'class': ' '.join(rid)}
            rowspan = idx_lengths.get((c, r), 0)
            if rowspan > 1:
                es['attributes'] = [format_attr({'key': 'rowspan', 'value': rowspan})]
            row_es.append(es)
        for c, col in enumerate(self.data.columns):
            cs = [DATA_CLASS, f'row{r}', f'col{c}']
            cs.extend(cell_context.get('data', {}).get(r, {}).get(c, []))
            formatter = self._display_funcs[r, c]
            value = self.data.iloc[r, c]
            row_dict = {'type': 'td', 'value': value, 'class': ' '.join(cs), 'display_value': formatter(value), 'is_visible': c not in hidden_columns}
            if self.cell_ids or not (len(ctx[r, c]) == 1 and ctx[r, c][0] == ''):
                row_dict['id'] = '_'.join(cs[1:])
            row_es.append(row_dict)
            props = []
            for x in ctx[r, c]:
                if x.count(':'):
                    props.append(x.split(':'))
                else:
                    props.append(['', ''])
            cellstyle.append({'props': props, 'selector': f'row{r}_col{c}'})
        body.append(row_es)
    table_attr = self.table_attributes
    use_mathjax = get_option('display.html.use_mathjax')
    if not use_mathjax:
        table_attr = table_attr or ''
        if 'class="' in table_attr:
            table_attr = table_attr.replace('class="', 'class="tex2jax_ignore ')
        else:
            table_attr += ' class="tex2jax_ignore"'
    return dict(head=head, cellstyle=cellstyle, body=body, uuid=uuid, precision=precision, table_styles=table_styles, caption=caption, table_attributes=table_attr)