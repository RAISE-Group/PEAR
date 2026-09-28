@pytest.mark.parametrize('op_name', ['union', 'intersection', 'difference', 'symmetric_difference'])
@pytest.mark.parametrize('sort', [None, False])
def test_set_incompatible_types(self, closed, op_name, sort):
    index = monotonic_index(0, 11, closed=closed)
    set_op = getattr(index, op_name)
    if op_name == 'difference':
        expected = index
    else:
        expected = getattr(index.astype('O'), op_name)(Index([1, 2, 3]))
    result = set_op(Index([1, 2, 3]), sort=sort)
    tm.assert_index_equal(result, expected)
    msg = 'can only do set operations between two IntervalIndex objects that are closed on the same side'
    for other_closed in {'right', 'left', 'both', 'neither'} - {closed}:
        other = monotonic_index(0, 11, closed=other_closed)
        with pytest.raises(ValueError, match=msg):
            set_op(other, sort=sort)
    other = interval_range(Timestamp('20180101'), periods=9, closed=closed)
    msg = 'can only do {op} between two IntervalIndex objects that have compatible dtypes'.format(op=op_name)
    with pytest.raises(TypeError, match=msg):
        set_op(other, sort=sort)