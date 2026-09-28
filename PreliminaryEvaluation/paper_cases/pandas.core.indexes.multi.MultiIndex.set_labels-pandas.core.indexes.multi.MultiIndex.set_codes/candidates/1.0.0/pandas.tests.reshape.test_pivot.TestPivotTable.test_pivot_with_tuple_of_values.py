@pytest.mark.parametrize('method', [True, False])
def test_pivot_with_tuple_of_values(self, method):
    df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'], 'bar': ['A', 'B', 'C', 'A', 'B', 'C'], 'baz': [1, 2, 3, 4, 5, 6], 'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
    with pytest.raises(KeyError, match="^\\('bar', 'baz'\\)$"):
        if method:
            df.pivot(index='zoo', columns='foo', values=('bar', 'baz'))
        else:
            pd.pivot(df, index='zoo', columns='foo', values=('bar', 'baz'))