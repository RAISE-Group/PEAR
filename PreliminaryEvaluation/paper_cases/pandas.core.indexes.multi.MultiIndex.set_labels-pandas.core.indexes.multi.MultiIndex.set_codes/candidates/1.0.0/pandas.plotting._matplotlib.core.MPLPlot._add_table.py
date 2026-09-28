def _add_table(self):
    if self.table is False:
        return
    elif self.table is True:
        data = self.data.transpose()
    else:
        data = self.table
    ax = self._get_ax(0)
    table(ax, data)