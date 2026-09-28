def test_isin_with_string_scalar(self):
    df = DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'], 'ids2': ['a', 'n', 'c', 'n']}, index=['foo', 'bar', 'baz', 'qux'])
    with pytest.raises(TypeError):
        df.isin('a')
    with pytest.raises(TypeError):
        df.isin('aaa')