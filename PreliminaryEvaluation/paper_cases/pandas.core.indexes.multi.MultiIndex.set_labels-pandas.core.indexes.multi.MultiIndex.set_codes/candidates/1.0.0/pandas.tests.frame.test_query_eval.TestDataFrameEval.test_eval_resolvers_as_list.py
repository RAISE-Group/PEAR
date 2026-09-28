def test_eval_resolvers_as_list(self):
    df = DataFrame(np.random.randn(10, 2), columns=list('ab'))
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    assert df.eval('a + b', resolvers=[dict1, dict2]) == dict1['a'] + dict2['b']
    assert pd.eval('a + b', resolvers=[dict1, dict2]) == dict1['a'] + dict2['b']