def _format_native_types(self, na_rep='nan', **kwargs):
    new_levels = []
    new_codes = []
    for level, level_codes in zip(self.levels, self.codes):
        level = level._format_native_types(na_rep=na_rep, **kwargs)
        mask = level_codes == -1
        if mask.any():
            nan_index = len(level)
            level = np.append(level, na_rep)
            assert not level_codes.flags.writeable
            level_codes = level_codes.copy()
            level_codes[mask] = nan_index
        new_levels.append(level)
        new_codes.append(level_codes)
    if len(new_levels) == 1:
        return Index(new_levels[0].take(new_codes[0]))._format_native_types()
    else:
        mi = MultiIndex(levels=new_levels, codes=new_codes, names=self.names, sortorder=self.sortorder, verify_integrity=False)
        return mi.values