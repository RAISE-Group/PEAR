def test_getitem_setitem_ix_bool_keyerror(self):
    df = DataFrame({'a': [1, 2, 3]})
    with pytest.raises(KeyError, match='^False$'):
        df.loc[False]
    with pytest.raises(KeyError, match='^True$'):
        df.loc[True]
    msg = 'cannot use a single bool to index into setitem'
    with pytest.raises(KeyError, match=msg):
        df.loc[False] = 0
    with pytest.raises(KeyError, match=msg):
        df.loc[True] = 0