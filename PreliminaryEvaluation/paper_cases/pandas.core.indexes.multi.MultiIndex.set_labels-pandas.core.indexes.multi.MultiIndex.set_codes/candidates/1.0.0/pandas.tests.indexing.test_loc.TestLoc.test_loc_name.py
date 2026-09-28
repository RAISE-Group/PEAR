def test_loc_name(self):
    df = DataFrame([[1, 1], [1, 1]])
    df.index.name = 'index_name'
    result = df.iloc[[0, 1]].index.name
    assert result == 'index_name'
    result = df.loc[[0, 1]].index.name
    assert result == 'index_name'