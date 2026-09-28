def _do_select_columns(self, data, columns):
    if not self._column_selector_set:
        column_set = set(columns)
        if len(column_set) != len(columns):
            raise ValueError('columns contains duplicate entries')
        unmatched = column_set.difference(data.columns)
        if unmatched:
            raise ValueError('The following columns were not found in the Stata data set: ' + ', '.join(list(unmatched)))
        dtyplist = []
        typlist = []
        fmtlist = []
        lbllist = []
        for col in columns:
            i = data.columns.get_loc(col)
            dtyplist.append(self.dtyplist[i])
            typlist.append(self.typlist[i])
            fmtlist.append(self.fmtlist[i])
            lbllist.append(self.lbllist[i])
        self.dtyplist = dtyplist
        self.typlist = typlist
        self.fmtlist = fmtlist
        self.lbllist = lbllist
        self._column_selector_set = True
    return data[columns]