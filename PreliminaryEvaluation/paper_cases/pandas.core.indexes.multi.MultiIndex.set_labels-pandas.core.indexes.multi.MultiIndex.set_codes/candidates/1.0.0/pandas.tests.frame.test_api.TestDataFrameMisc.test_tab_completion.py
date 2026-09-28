def test_tab_completion(self):
    df = pd.DataFrame([list('abcd'), list('efgh')], columns=list('ABCD'))
    for key in list('ABCD'):
        assert key in dir(df)
    assert isinstance(df.__getitem__('A'), pd.Series)
    df = pd.DataFrame([list('abcd'), list('efgh')], columns=pd.MultiIndex.from_tuples(list(zip('ABCD', 'EFGH'))))
    for key in list('ABCD'):
        assert key in dir(df)
    for key in list('EFGH'):
        assert key not in dir(df)
    assert isinstance(df.__getitem__('A'), pd.DataFrame)