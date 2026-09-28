def remove_unused_levels(self):
    """
        Create a new MultiIndex from the current that removes
        unused levels, meaning that they are not expressed in the labels.

        The resulting MultiIndex will have the same outward
        appearance, meaning the same .values and ordering. It will also
        be .equals() to the original.

        Returns
        -------
        MultiIndex

        Examples
        --------
        >>> mi = pd.MultiIndex.from_product([range(2), list('ab')])
        >>> mi
        MultiIndex([(0, 'a'),
                    (0, 'b'),
                    (1, 'a'),
                    (1, 'b')],
                   )

        >>> mi[2:]
        MultiIndex([(1, 'a'),
                    (1, 'b')],
                   )

        The 0 from the first level is not represented
        and can be removed

        >>> mi2 = mi[2:].remove_unused_levels()
        >>> mi2.levels
        FrozenList([[1], ['a', 'b']])
        """
    new_levels = []
    new_codes = []
    changed = False
    for lev, level_codes in zip(self.levels, self.codes):
        uniques = np.where(np.bincount(level_codes + 1) > 0)[0] - 1
        has_na = int(len(uniques) and uniques[0] == -1)
        if len(uniques) != len(lev) + has_na:
            changed = True
            uniques = algos.unique(level_codes)
            if has_na:
                na_idx = np.where(uniques == -1)[0]
                uniques[[0, na_idx[0]]] = uniques[[na_idx[0], 0]]
            code_mapping = np.zeros(len(lev) + has_na)
            code_mapping[uniques] = np.arange(len(uniques)) - has_na
            level_codes = code_mapping[level_codes]
            lev = lev.take(uniques[has_na:])
        new_levels.append(lev)
        new_codes.append(level_codes)
    result = self.view()
    if changed:
        result._reset_identity()
        result._set_levels(new_levels, validate=False)
        result._set_codes(new_codes, validate=False)
    return result