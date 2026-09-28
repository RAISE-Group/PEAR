def where(self, other, cond, align=True, errors='raise', try_cast: bool=False, axis: int=0) -> List['Block']:
    if isinstance(other, ABCDataFrame):
        assert other.shape[1] == 1
        other = other.iloc[:, 0]
    other = extract_array(other, extract_numpy=True)
    if isinstance(cond, ABCDataFrame):
        assert cond.shape[1] == 1
        cond = cond.iloc[:, 0]
    cond = extract_array(cond, extract_numpy=True)
    if lib.is_scalar(other) and isna(other):
        other = self.dtype.na_value
    if is_sparse(self.values):
        dtype = None
    else:
        dtype = self.dtype
    result = self.values.copy()
    icond = ~cond
    if lib.is_scalar(other):
        set_other = other
    else:
        set_other = other[icond]
    try:
        result[icond] = set_other
    except (NotImplementedError, TypeError):
        result = self._holder._from_sequence(np.where(cond, self.values, other), dtype=dtype)
    return [self.make_block_same_class(result, placement=self.mgr_locs)]