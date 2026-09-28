@classmethod
def _add_numeric_methods_binary(cls):
    """ add in numeric methods, specialized to RangeIndex """

    def _make_evaluate_binop(op, step=False):
        """
            Parameters
            ----------
            op : callable that accepts 2 parms
                perform the binary op
            step : callable, optional, default to False
                op to apply to the step parm if not None
                if False, use the existing step
            """

        @unpack_zerodim_and_defer(op.__name__)
        def _evaluate_numeric_binop(self, other):
            if isinstance(other, ABCTimedeltaIndex):
                return NotImplemented
            elif isinstance(other, (timedelta, np.timedelta64)):
                return op(self._int64index, other)
            elif is_timedelta64_dtype(other):
                return op(self._int64index, other)
            other = extract_array(other, extract_numpy=True)
            attrs = self._get_attributes_dict()
            left, right = (self, other)
            try:
                if step:
                    with np.errstate(all='ignore'):
                        rstep = step(left.step, right)
                    if not is_integer(rstep) or not rstep:
                        raise ValueError
                else:
                    rstep = left.step
                with np.errstate(all='ignore'):
                    rstart = op(left.start, right)
                    rstop = op(left.stop, right)
                result = type(self)(rstart, rstop, rstep, **attrs)
                if not all((is_integer(x) for x in [rstart, rstop, rstep])):
                    result = result.astype('float64')
                return result
            except (ValueError, TypeError, ZeroDivisionError):
                return op(self._int64index, other)
        name = f'__{op.__name__}__'
        return compat.set_function_name(_evaluate_numeric_binop, name, cls)
    cls.__add__ = _make_evaluate_binop(operator.add)
    cls.__radd__ = _make_evaluate_binop(ops.radd)
    cls.__sub__ = _make_evaluate_binop(operator.sub)
    cls.__rsub__ = _make_evaluate_binop(ops.rsub)
    cls.__mul__ = _make_evaluate_binop(operator.mul, step=operator.mul)
    cls.__rmul__ = _make_evaluate_binop(ops.rmul, step=ops.rmul)
    cls.__truediv__ = _make_evaluate_binop(operator.truediv, step=operator.truediv)
    cls.__rtruediv__ = _make_evaluate_binop(ops.rtruediv, step=ops.rtruediv)