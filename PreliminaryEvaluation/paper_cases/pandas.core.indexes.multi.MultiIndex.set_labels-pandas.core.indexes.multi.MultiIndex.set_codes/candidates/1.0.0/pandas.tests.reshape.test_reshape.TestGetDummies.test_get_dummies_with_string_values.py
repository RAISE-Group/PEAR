@pytest.mark.parametrize('values', ['baz'])
def test_get_dummies_with_string_values(self, values):
    df = pd.DataFrame({'bar': [1, 2, 3, 4, 5, 6], 'foo': ['one', 'one', 'one', 'two', 'two', 'two'], 'baz': ['A', 'B', 'C', 'A', 'B', 'C'], 'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
    msg = 'Input must be a list-like for parameter `columns`'
    with pytest.raises(TypeError, match=msg):
        pd.get_dummies(df, columns=values)