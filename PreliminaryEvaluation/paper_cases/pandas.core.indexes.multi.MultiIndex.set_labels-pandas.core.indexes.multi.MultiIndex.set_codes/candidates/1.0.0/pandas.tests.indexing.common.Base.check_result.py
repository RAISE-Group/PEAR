def check_result(self, method1, key1, method2, key2, typs=None, axes=None, fails=None):

    def _eq(axis, obj, key1, key2):
        """ compare equal for these 2 keys """
        if axis > obj.ndim - 1:
            return
        try:
            rs = getattr(obj, method1).__getitem__(_axify(obj, key1, axis))
            try:
                xp = self.get_result(obj=obj, method=method2, key=key2, axis=axis)
            except (KeyError, IndexError):
                return
            if is_scalar(rs) and is_scalar(xp):
                assert rs == xp
            else:
                tm.assert_equal(rs, xp)
        except (IndexError, TypeError, KeyError) as detail:
            if fails is not None:
                if isinstance(detail, fails):
                    result = f'ok ({type(detail).__name__})'
                    return
            result = type(detail).__name__
            raise AssertionError(result, detail)
    if typs is None:
        typs = self._typs
    if axes is None:
        axes = [0, 1]
    elif not isinstance(axes, (tuple, list)):
        assert isinstance(axes, int)
        axes = [axes]
    for kind in self._kinds:
        d = getattr(self, kind)
        for ax in axes:
            for typ in typs:
                if typ not in self._typs:
                    continue
                obj = d[typ]
                _eq(axis=ax, obj=obj, key1=key1, key2=key2)