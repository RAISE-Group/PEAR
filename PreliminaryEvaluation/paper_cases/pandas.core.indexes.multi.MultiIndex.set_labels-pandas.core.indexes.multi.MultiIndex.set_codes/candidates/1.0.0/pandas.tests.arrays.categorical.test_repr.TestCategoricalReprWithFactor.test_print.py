def test_print(self):
    expected = ['[a, b, b, a, a, c, c, c]', 'Categories (3, object): [a < b < c]']
    expected = '\n'.join(expected)
    actual = repr(self.factor)
    assert actual == expected