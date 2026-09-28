def test_insert_error_msmgs(self):
    df = DataFrame({'foo': ['a', 'b', 'c'], 'bar': [1, 2, 3], 'baz': ['d', 'e', 'f']}).set_index('foo')
    s = DataFrame({'foo': ['a', 'b', 'c', 'a'], 'fiz': ['g', 'h', 'i', 'j']}).set_index('foo')
    msg = 'cannot reindex from a duplicate axis'
    with pytest.raises(ValueError, match=msg):
        df['newcol'] = s
    df = DataFrame(np.random.randint(0, 2, (4, 4)), columns=['a', 'b', 'c', 'd'])
    msg = 'incompatible index of inserted column with frame index'
    with pytest.raises(TypeError, match=msg):
        df['gr'] = df.groupby(['b', 'c']).count()