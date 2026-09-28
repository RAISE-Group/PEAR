def _python_agg_general(self, func, *args, **kwargs):
    func = self._is_builtin_func(func)
    f = lambda x: func(x, *args, **kwargs)
    output: Dict[base.OutputKey, np.ndarray] = {}
    for idx, obj in enumerate(self._iterate_slices()):
        name = obj.name
        if self.grouper.ngroups == 0:
            continue
        try:
            func(obj[:0])
        except TypeError:
            continue
        except AssertionError:
            raise
        except Exception:
            pass
        result, counts = self.grouper.agg_series(obj, f)
        assert result is not None
        key = base.OutputKey(label=name, position=idx)
        output[key] = self._try_cast(result, obj, numeric_only=True)
    if len(output) == 0:
        return self._python_apply_general(f)
    if self.grouper._filter_empty_groups:
        mask = counts.ravel() > 0
        for key, result in output.items():
            values = result
            if is_numeric_dtype(values.dtype):
                values = ensure_float(values)
            output[key] = self._try_cast(values[mask], result)
    return self._wrap_aggregated_output(output)