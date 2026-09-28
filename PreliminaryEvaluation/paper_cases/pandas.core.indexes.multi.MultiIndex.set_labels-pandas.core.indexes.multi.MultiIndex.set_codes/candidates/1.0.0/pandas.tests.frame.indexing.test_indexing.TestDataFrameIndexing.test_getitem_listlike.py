@pytest.mark.parametrize('idx_type', [list, iter, Index, set, lambda l: dict(zip(l, range(len(l)))), lambda l: dict(zip(l, range(len(l)))).keys()], ids=['list', 'iter', 'Index', 'set', 'dict', 'dict_keys'])
@pytest.mark.parametrize('levels', [1, 2])
def test_getitem_listlike(self, idx_type, levels, float_frame):
    if levels == 1:
        frame, missing = (float_frame, 'food')
    else:
        frame = DataFrame(np.random.randn(8, 3), columns=Index([('foo', 'bar'), ('baz', 'qux'), ('peek', 'aboo')], name=('sth', 'sth2')))
        missing = ('good', 'food')
    keys = [frame.columns[1], frame.columns[0]]
    idx = idx_type(keys)
    idx_check = list(idx_type(keys))
    result = frame[idx]
    expected = frame.loc[:, idx_check]
    expected.columns.names = frame.columns.names
    tm.assert_frame_equal(result, expected)
    idx = idx_type(keys + [missing])
    with pytest.raises(KeyError, match='not in index'):
        frame[idx]