def _repr_categories_info(self) -> str:
    """
        Returns a string representation of the footer.
        """
    category_strs = self._repr_categories()
    dtype = str(self.categories.dtype)
    levheader = f'Categories ({len(self.categories)}, {dtype}): '
    width, height = get_terminal_size()
    max_width = get_option('display.width') or width
    if console.in_ipython_frontend():
        max_width = 0
    levstring = ''
    start = True
    cur_col_len = len(levheader)
    sep_len, sep = (3, ' < ') if self.ordered else (2, ', ')
    linesep = sep.rstrip() + '\n'
    for val in category_strs:
        if max_width != 0 and cur_col_len + sep_len + len(val) > max_width:
            levstring += linesep + ' ' * (len(levheader) + 1)
            cur_col_len = len(levheader) + 1
        elif not start:
            levstring += sep
            cur_col_len += len(val)
        levstring += val
        start = False
    return levheader + '[' + levstring.replace(' < ... < ', ' ... ') + ']'