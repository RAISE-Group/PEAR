def _check_op(self, s, op_name, other, exc=None):
    op = self.get_op_from_name(op_name)
    result = op(s, other)
    mask = s.isna()
    if isinstance(s, pd.DataFrame):
        result = result.squeeze()
        s = s.squeeze()
        mask = mask.squeeze()
    if isinstance(other, IntegerArray):
        omask = getattr(other, 'mask', None)
        mask = getattr(other, 'data', other)
        if omask is not None:
            mask |= omask
    if op_name == '__pow__':
        mask = np.where(~s.isna() & (s == 1), False, mask)
    elif op_name == '__rpow__':
        other_is_one = other == 1
        if isinstance(other_is_one, pd.Series):
            other_is_one = other_is_one.fillna(False)
        mask = np.where(other_is_one, False, mask)
    if is_float_dtype(other) or is_float(other) or op_name in ['__rtruediv__', '__truediv__', '__rdiv__', '__div__']:
        rs = s.astype('float')
        expected = op(rs, other)
        self._check_op_float(result, expected, mask, s, op_name, other)
    else:
        rs = pd.Series(s.values._data, name=s.name)
        expected = op(rs, other)
        self._check_op_integer(result, expected, mask, s, op_name, other)