@classmethod
@Appender(_interval_shared_docs['from_tuples'] % dict(klass='IntervalIndex', examples=textwrap.dedent("        Examples\n        --------\n        >>> pd.IntervalIndex.from_tuples([(0, 1), (1, 2)])\n        IntervalIndex([(0, 1], (1, 2]],\n                       closed='right',\n                       dtype='interval[int64]')\n        ")))
def from_tuples(cls, data, closed: str='right', name=None, copy: bool=False, dtype=None):
    with rewrite_exception('IntervalArray', cls.__name__):
        arr = IntervalArray.from_tuples(data, closed=closed, copy=copy, dtype=dtype)
    return cls._simple_new(arr, name=name)