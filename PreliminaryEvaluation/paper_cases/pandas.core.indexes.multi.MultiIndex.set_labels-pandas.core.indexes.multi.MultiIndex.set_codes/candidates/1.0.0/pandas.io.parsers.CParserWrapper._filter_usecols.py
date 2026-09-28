def _filter_usecols(self, names):
    usecols = _evaluate_usecols(self.usecols, names)
    if usecols is not None and len(names) != len(usecols):
        names = [name for i, name in enumerate(names) if i in usecols or name in usecols]
    return names