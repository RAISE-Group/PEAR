@pytest.mark.parametrize('values', [['baz', 'zoo'], np.array(['baz', 'zoo']), pd.Series(['baz', 'zoo']), pd.Index(['baz', 'zoo'])])
@pytest.mark.parametrize('method', [True, False])
def test_pivot_with_list_like_values(self, values, method):
    df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'], 'bar': ['A', 'B', 'C', 'A', 'B', 'C'], 'baz': [1, 2, 3, 4, 5, 6], 'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
    if method:
        result = df.pivot(index='foo', columns='bar', values=values)
    else:
        result = pd.pivot(df, index='foo', columns='bar', values=values)
    data = [[1, 2, 3, 'x', 'y', 'z'], [4, 5, 6, 'q', 'w', 't']]
    index = Index(data=['one', 'two'], name='foo')
    columns = MultiIndex(levels=[['baz', 'zoo'], ['A', 'B', 'C']], codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]], names=[None, 'bar'])
    expected = DataFrame(data=data, index=index, columns=columns, dtype='object')
    tm.assert_frame_equal(result, expected)