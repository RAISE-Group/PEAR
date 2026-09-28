def _search_replace_num_columns(self, lines, search, replace):
    ret = []
    for l in lines:
        rl = []
        for i, x in enumerate(l):
            if not isinstance(x, str) or search not in x or (self._no_thousands_columns and i in self._no_thousands_columns) or self.nonnum.search(x.strip()):
                rl.append(x)
            else:
                rl.append(x.replace(search, replace))
        ret.append(rl)
    return ret