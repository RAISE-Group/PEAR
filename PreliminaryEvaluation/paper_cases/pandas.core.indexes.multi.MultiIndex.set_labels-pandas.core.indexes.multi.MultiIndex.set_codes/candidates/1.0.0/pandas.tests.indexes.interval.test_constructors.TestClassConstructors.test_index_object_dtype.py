@pytest.mark.parametrize('values_constructor', [list, np.array, IntervalIndex, IntervalArray])
def test_index_object_dtype(self, values_constructor):
    intervals = [Interval(0, 1), Interval(1, 2), Interval(2, 3)]
    values = values_constructor(intervals)
    result = Index(values, dtype=object)
    assert type(result) is Index
    tm.assert_numpy_array_equal(result.values, np.array(values))