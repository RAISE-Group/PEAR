@Appender(_interval_shared_docs['overlaps'] % dict(klass='IntervalArray', examples=textwrap.dedent('        >>> data = [(0, 1), (1, 3), (2, 4)]\n        >>> intervals = pd.arrays.IntervalArray.from_tuples(data)\n        >>> intervals\n        <IntervalArray>\n        [(0, 1], (1, 3], (2, 4]]\n        Length: 3, closed: right, dtype: interval[int64]\n        ')))
def overlaps(self, other):
    if isinstance(other, (IntervalArray, ABCIntervalIndex)):
        raise NotImplementedError
    elif not isinstance(other, Interval):
        msg = f'`other` must be Interval-like, got {type(other).__name__}'
        raise TypeError(msg)
    op1 = le if self.closed_left and other.closed_right else lt
    op2 = le if other.closed_left and self.closed_right else lt
    return op1(self.left, other.right) & op2(other.left, self.right)