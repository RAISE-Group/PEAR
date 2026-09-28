@pytest.mark.parametrize('method', ['stack', 'unstack'])
def test_stack_unstack_wrong_level_name(self, method):
    df = self.frame.loc['foo']
    with pytest.raises(KeyError, match='does not match index name'):
        getattr(df, method)('mistake')
    if method == 'unstack':
        s = df.iloc[:, 0]
        with pytest.raises(KeyError, match='does not match index name'):
            getattr(s, method)('mistake')