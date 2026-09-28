@classmethod
@Appender(_interval_shared_docs['from_tuples'] % dict(klass='IntervalArray', examples=textwrap.dedent('        Examples\n        --------\n        >>> pd.arrays.IntervalArray.from_tuples([(0, 1), (1, 2)])\n        <IntervalArray>\n        [(0, 1], (1, 2]]\n        Length: 2, closed: right, dtype: interval[int64]\n        ')))
def from_tuples(cls, data, closed='right', copy=False, dtype=None):
    if len(data):
        left, right = ([], [])
    else:
        left = right = data
    for d in data:
        if isna(d):
            lhs = rhs = np.nan
        else:
            name = cls.__name__
            try:
                lhs, rhs = d
            except ValueError:
                msg = f'{name}.from_tuples requires tuples of length 2, got {d}'
                raise ValueError(msg)
            except TypeError:
                msg = f'{name}.from_tuples received an invalid item, {d}'
                raise TypeError(msg)
        left.append(lhs)
        right.append(rhs)
    return cls.from_arrays(left, right, closed, copy=False, dtype=dtype)