def _expand_colspan_rowspan(self, rows):
    """
        Given a list of <tr>s, return a list of text rows.

        Parameters
        ----------
        rows : list of node-like
            List of <tr>s

        Returns
        -------
        list of list
            Each returned row is a list of str text.

        Notes
        -----
        Any cell with ``rowspan`` or ``colspan`` will have its contents copied
        to subsequent cells.
        """
    all_texts = []
    remainder = []
    for tr in rows:
        texts = []
        next_remainder = []
        index = 0
        tds = self._parse_td(tr)
        for td in tds:
            while remainder and remainder[0][0] <= index:
                prev_i, prev_text, prev_rowspan = remainder.pop(0)
                texts.append(prev_text)
                if prev_rowspan > 1:
                    next_remainder.append((prev_i, prev_text, prev_rowspan - 1))
                index += 1
            text = _remove_whitespace(self._text_getter(td))
            rowspan = int(self._attr_getter(td, 'rowspan') or 1)
            colspan = int(self._attr_getter(td, 'colspan') or 1)
            for _ in range(colspan):
                texts.append(text)
                if rowspan > 1:
                    next_remainder.append((index, text, rowspan - 1))
                index += 1
        for prev_i, prev_text, prev_rowspan in remainder:
            texts.append(prev_text)
            if prev_rowspan > 1:
                next_remainder.append((prev_i, prev_text, prev_rowspan - 1))
        all_texts.append(texts)
        remainder = next_remainder
    while remainder:
        next_remainder = []
        texts = []
        for prev_i, prev_text, prev_rowspan in remainder:
            texts.append(prev_text)
            if prev_rowspan > 1:
                next_remainder.append((prev_i, prev_text, prev_rowspan - 1))
        all_texts.append(texts)
        remainder = next_remainder
    return all_texts