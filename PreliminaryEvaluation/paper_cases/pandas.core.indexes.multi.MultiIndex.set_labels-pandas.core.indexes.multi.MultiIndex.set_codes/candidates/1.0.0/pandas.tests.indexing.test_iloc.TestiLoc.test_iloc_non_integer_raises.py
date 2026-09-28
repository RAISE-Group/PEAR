@pytest.mark.parametrize('index,columns', [(np.arange(20), list('ABCDE'))])
@pytest.mark.parametrize('index_vals,column_vals', [[slice(None), ['A', 'D']], (['1', '2'], slice(None)), ([datetime(2019, 1, 1)], slice(None))])
def test_iloc_non_integer_raises(self, index, columns, index_vals, column_vals):
    df = DataFrame(np.random.randn(len(index), len(columns)), index=index, columns=columns)
    msg = '.iloc requires numeric indexers, got'
    with pytest.raises(IndexError, match=msg):
        df.iloc[index_vals, column_vals]