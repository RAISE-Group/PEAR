def check_results(self, targ, res, axis, check_dtype=True):
    res = getattr(res, 'asm8', res)
    res = getattr(res, 'values', res)

    def _coerce_tds(targ, res):
        if hasattr(targ, 'dtype') and targ.dtype == 'm8[ns]':
            if len(targ) == 1:
                targ = targ[0].item()
                res = res.item()
            else:
                targ = targ.view('i8')
        return (targ, res)
    try:
        if axis != 0 and hasattr(targ, 'shape') and targ.ndim and (targ.shape != res.shape):
            res = np.split(res, [targ.shape[0]], axis=0)[0]
    except (ValueError, IndexError):
        targ, res = _coerce_tds(targ, res)
    try:
        tm.assert_almost_equal(targ, res, check_dtype=check_dtype)
    except AssertionError:
        if hasattr(targ, 'dtype') and targ.dtype == 'm8[ns]':
            targ, res = _coerce_tds(targ, res)
            tm.assert_almost_equal(targ, res, check_dtype=check_dtype)
            return
        if not hasattr(res, 'dtype') or res.dtype.kind not in ['c', 'O']:
            raise
        if res.dtype.kind == 'O':
            if targ.dtype.kind != 'O':
                res = res.astype(targ.dtype)
            else:
                cast_dtype = 'c16' if has_c16 else 'f8'
                res = res.astype(cast_dtype)
                targ = targ.astype(cast_dtype)
        elif targ.dtype.kind == 'O':
            raise
        tm.assert_almost_equal(np.real(targ), np.real(res), check_dtype=check_dtype)
        tm.assert_almost_equal(np.imag(targ), np.imag(res), check_dtype=check_dtype)