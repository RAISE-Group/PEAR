def _update_strl_names(self):
    """Update column names for conversion to strl if they might have been
        changed to comply with Stata naming rules"""
    for orig, new in self._converted_names.items():
        if orig in self._convert_strl:
            idx = self._convert_strl.index(orig)
            self._convert_strl[idx] = new