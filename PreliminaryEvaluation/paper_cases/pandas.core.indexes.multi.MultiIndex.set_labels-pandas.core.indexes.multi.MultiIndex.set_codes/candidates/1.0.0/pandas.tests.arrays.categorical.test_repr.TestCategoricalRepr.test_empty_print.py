def test_empty_print(self):
    factor = Categorical([], ['a', 'b', 'c'])
    expected = '[], Categories (3, object): [a, b, c]'
    actual = repr(factor)
    assert actual == expected
    assert expected == actual
    factor = Categorical([], ['a', 'b', 'c'], ordered=True)
    expected = '[], Categories (3, object): [a < b < c]'
    actual = repr(factor)
    assert expected == actual
    factor = Categorical([], [])
    expected = '[], Categories (0, object): []'
    assert expected == repr(factor)