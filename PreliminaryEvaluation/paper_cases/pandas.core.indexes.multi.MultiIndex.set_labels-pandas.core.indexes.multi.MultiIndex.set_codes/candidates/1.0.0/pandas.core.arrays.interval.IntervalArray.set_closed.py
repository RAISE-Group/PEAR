@Appender(_interval_shared_docs['set_closed'] % dict(klass='IntervalArray', examples=textwrap.dedent("        Examples\n        --------\n        >>> index = pd.arrays.IntervalArray.from_breaks(range(4))\n        >>> index\n        <IntervalArray>\n        [(0, 1], (1, 2], (2, 3]]\n        Length: 3, closed: right, dtype: interval[int64]\n        >>> index.set_closed('both')\n        <IntervalArray>\n        [[0, 1], [1, 2], [2, 3]]\n        Length: 3, closed: both, dtype: interval[int64]\n        ")))
def set_closed(self, closed):
    if closed not in _VALID_CLOSED:
        msg = f"invalid option for 'closed': {closed}"
        raise ValueError(msg)
    return self._shallow_copy(closed=closed)