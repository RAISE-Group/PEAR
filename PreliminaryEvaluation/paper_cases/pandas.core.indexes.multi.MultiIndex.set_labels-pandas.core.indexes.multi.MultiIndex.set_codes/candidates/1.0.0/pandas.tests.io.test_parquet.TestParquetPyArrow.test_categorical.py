def test_categorical(self, pa):
    df = pd.DataFrame()
    df['a'] = pd.Categorical(list('abcdef'))
    df['b'] = pd.Categorical(['bar', 'foo', 'foo', 'bar', None, 'bar'], dtype=pd.CategoricalDtype(['foo', 'bar', 'baz']))
    df['c'] = pd.Categorical(['a', 'b', 'c', 'a', 'c', 'b'], categories=['b', 'c', 'd'], ordered=True)
    if LooseVersion(pyarrow.__version__) >= LooseVersion('0.15.0'):
        check_round_trip(df, pa)
    else:
        expected = df.astype(object)
        check_round_trip(df, pa, expected=expected)