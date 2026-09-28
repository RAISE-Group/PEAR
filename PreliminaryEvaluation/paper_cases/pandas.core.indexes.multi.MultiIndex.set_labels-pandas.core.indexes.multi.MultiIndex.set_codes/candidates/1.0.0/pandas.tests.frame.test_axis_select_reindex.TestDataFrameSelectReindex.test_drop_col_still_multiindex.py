def test_drop_col_still_multiindex(self):
    arrays = [['a', 'b', 'c', 'top'], ['', '', '', 'OD'], ['', '', '', 'wx']]
    tuples = sorted(zip(*arrays))
    index = MultiIndex.from_tuples(tuples)
    df = DataFrame(np.random.randn(3, 4), columns=index)
    del df['a', '', '']
    assert isinstance(df.columns, MultiIndex)