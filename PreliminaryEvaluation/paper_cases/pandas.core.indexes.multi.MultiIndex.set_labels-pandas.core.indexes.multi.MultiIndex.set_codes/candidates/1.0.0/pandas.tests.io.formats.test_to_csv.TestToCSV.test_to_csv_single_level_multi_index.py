@pytest.mark.parametrize('ind,expected', [(pd.MultiIndex(levels=[[1.0]], codes=[[0]], names=['x']), 'x,data\n1.0,1\n'), (pd.MultiIndex(levels=[[1.0], [2.0]], codes=[[0], [0]], names=['x', 'y']), 'x,y,data\n1.0,2.0,1\n')])
@pytest.mark.parametrize('klass', [pd.DataFrame, pd.Series])
def test_to_csv_single_level_multi_index(self, ind, expected, klass):
    result = klass(pd.Series([1], ind, name='data')).to_csv(line_terminator='\n', header=True)
    assert result == expected