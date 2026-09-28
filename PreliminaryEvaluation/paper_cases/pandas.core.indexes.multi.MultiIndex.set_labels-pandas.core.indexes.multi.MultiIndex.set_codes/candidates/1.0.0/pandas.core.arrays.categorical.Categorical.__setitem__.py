def __setitem__(self, key, value):
    """
        Item assignment.

        Raises
        ------
        ValueError
            If (one or more) Value is not in categories or if a assigned
            `Categorical` does not have the same categories
        """
    value = extract_array(value, extract_numpy=True)
    if isinstance(value, Categorical):
        if not is_dtype_equal(self, value):
            raise ValueError('Cannot set a Categorical with another, without identical categories')
        if not self.categories.equals(value.categories):
            new_codes = _recode_for_categories(value.codes, value.categories, self.categories)
            value = Categorical.from_codes(new_codes, dtype=self.dtype)
    rvalue = value if is_list_like(value) else [value]
    from pandas import Index
    to_add = Index(rvalue).difference(self.categories)
    if len(to_add) and (not isna(to_add).all()):
        raise ValueError('Cannot setitem on a Categorical with a new category, set the categories first')
    if isinstance(key, (int, np.integer)):
        pass
    elif isinstance(key, tuple):
        if len(key) == 2:
            if not com.is_null_slice(key[0]):
                raise AssertionError('invalid slicing for a 1-ndim categorical')
            key = key[1]
        elif len(key) == 1:
            key = key[0]
        else:
            raise AssertionError('invalid slicing for a 1-ndim categorical')
    elif isinstance(key, slice):
        pass
    lindexer = self.categories.get_indexer(rvalue)
    lindexer = self._maybe_coerce_indexer(lindexer)
    self._codes[key] = lindexer