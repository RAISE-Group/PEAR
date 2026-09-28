def test_concat_rename_index(self):
    a = DataFrame(np.random.rand(3, 3), columns=list('ABC'), index=Index(list('abc'), name='index_a'))
    b = DataFrame(np.random.rand(3, 3), columns=list('ABC'), index=Index(list('abc'), name='index_b'))
    result = concat([a, b], keys=['key0', 'key1'], names=['lvl0', 'lvl1'])
    exp = concat([a, b], keys=['key0', 'key1'], names=['lvl0'])
    names = list(exp.index.names)
    names[1] = 'lvl1'
    exp.index.set_names(names, inplace=True)
    tm.assert_frame_equal(result, exp)
    assert result.index.names == exp.index.names