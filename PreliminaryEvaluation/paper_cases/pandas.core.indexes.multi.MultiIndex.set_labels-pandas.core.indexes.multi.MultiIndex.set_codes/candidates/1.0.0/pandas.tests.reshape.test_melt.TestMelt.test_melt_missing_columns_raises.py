def test_melt_missing_columns_raises(self):
    df = pd.DataFrame(np.random.randn(5, 4), columns=list('abcd'))
    msg = "The following '{Var}' are not present in the DataFrame: {Col}"
    with pytest.raises(KeyError, match=msg.format(Var='value_vars', Col="\\['C'\\]")):
        df.melt(['a', 'b'], ['C', 'd'])
    with pytest.raises(KeyError, match=msg.format(Var='id_vars', Col="\\['A'\\]")):
        df.melt(['A', 'b'], ['c', 'd'])
    with pytest.raises(KeyError, match=msg.format(Var='id_vars', Col="\\['not_here', 'or_there'\\]")):
        df.melt(['a', 'b', 'not_here', 'or_there'], ['c', 'd'])
    multi = df.copy()
    multi.columns = [list('ABCD'), list('abcd')]
    with pytest.raises(KeyError, match=msg.format(Var='id_vars', Col="\\['E'\\]")):
        multi.melt([('E', 'a')], [('B', 'b')])
    with pytest.raises(KeyError, match=msg.format(Var='value_vars', Col="\\['F'\\]")):
        multi.melt(['A'], ['F'], col_level=0)