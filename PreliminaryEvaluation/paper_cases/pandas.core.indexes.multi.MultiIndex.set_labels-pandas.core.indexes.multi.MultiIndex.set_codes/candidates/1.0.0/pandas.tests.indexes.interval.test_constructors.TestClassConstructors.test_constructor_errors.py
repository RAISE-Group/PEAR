def test_constructor_errors(self, constructor):
    ivs = [Interval(0, 1, closed='right'), Interval(2, 3, closed='left')]
    msg = 'intervals must all be closed on the same side'
    with pytest.raises(ValueError, match=msg):
        constructor(ivs)
    msg = 'IntervalIndex\\(...\\) must be called with a collection of some kind, 5 was passed'
    with pytest.raises(TypeError, match=msg):
        constructor(5)
    msg = "type <class 'numpy.int64'> with value 0 is not an interval"
    with pytest.raises(TypeError, match=msg):
        constructor([0, 1])