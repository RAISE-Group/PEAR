def test_query_inplace(self):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    expected = df.copy()
    expected = expected[expected['a'] == 2]
    df.query('a == 2', inplace=True)
    tm.assert_frame_equal(expected, df)
    df = {}
    expected = {'a': 3}
    self.eval('a = 1 + 2', target=df, inplace=True)
    tm.assert_dict_equal(df, expected)