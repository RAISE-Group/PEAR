def test_mangle_dupe_cols_false(self):
    data = 'a b c\n1 2 3'
    msg = 'is not supported'
    for engine in ('c', 'python'):
        with pytest.raises(ValueError, match=msg):
            read_csv(StringIO(data), engine=engine, mangle_dupe_cols=False)