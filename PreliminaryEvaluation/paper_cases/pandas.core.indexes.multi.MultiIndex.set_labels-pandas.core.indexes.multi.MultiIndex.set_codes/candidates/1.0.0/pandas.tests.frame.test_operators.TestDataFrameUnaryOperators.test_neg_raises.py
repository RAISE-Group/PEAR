@pytest.mark.parametrize('df', [pd.DataFrame({'a': ['a', 'b']}), pd.DataFrame({'a': pd.to_datetime(['2017-01-22', '1970-01-01'])})])
def test_neg_raises(self, df):
    with pytest.raises(TypeError):
        -df
    with pytest.raises(TypeError):
        -df['a']