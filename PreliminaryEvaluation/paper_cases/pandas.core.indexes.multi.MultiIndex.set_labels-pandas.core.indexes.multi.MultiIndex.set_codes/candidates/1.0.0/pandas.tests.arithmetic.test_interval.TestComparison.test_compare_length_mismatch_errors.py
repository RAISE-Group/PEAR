@pytest.mark.parametrize('length', [1, 3, 5])
@pytest.mark.parametrize('other_constructor', [IntervalArray, list])
def test_compare_length_mismatch_errors(self, op, other_constructor, length):
    array = IntervalArray.from_arrays(range(4), range(1, 5))
    other = other_constructor([Interval(0, 1)] * length)
    with pytest.raises(ValueError, match='Lengths must match to compare'):
        op(array, other)