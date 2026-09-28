def _copy(self, deepcopy=False):
    styler = Styler(self.data, precision=self.precision, caption=self.caption, uuid=self.uuid, table_styles=self.table_styles, na_rep=self.na_rep)
    if deepcopy:
        styler.ctx = copy.deepcopy(self.ctx)
        styler._todo = copy.deepcopy(self._todo)
    else:
        styler.ctx = self.ctx
        styler._todo = self._todo
    return styler