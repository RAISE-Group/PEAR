def test_repr_truncation_column_size(self):
    df = pd.DataFrame({'a': [108480, 30830], 'b': [12345, 12345], 'c': [12345, 12345], 'd': [12345, 12345], 'e': ['a' * 50] * 2})
    assert '...' in str(df)
    assert '    ...    ' not in str(df)