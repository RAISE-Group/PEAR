def test_append_sorts(self, sort):
    df1 = pd.DataFrame({'a': [1, 2], 'b': [1, 2]}, columns=['b', 'a'])
    df2 = pd.DataFrame({'a': [1, 2], 'c': [3, 4]}, index=[2, 3])
    with tm.assert_produces_warning(None):
        result = df1.append(df2, sort=sort)
    expected = pd.DataFrame({'b': [1, 2, None, None], 'a': [1, 2, 1, 2], 'c': [None, None, 3, 4]}, columns=['a', 'b', 'c'])
    if sort is False:
        expected = expected[['b', 'a', 'c']]
    tm.assert_frame_equal(result, expected)