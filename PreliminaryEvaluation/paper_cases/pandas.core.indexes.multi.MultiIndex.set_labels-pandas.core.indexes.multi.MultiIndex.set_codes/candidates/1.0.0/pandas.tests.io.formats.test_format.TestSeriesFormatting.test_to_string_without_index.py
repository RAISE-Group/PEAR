def test_to_string_without_index(self):
    s = Series([1, 2, 3, 4])
    result = s.to_string(index=False)
    expected = ' 1\n' + ' 2\n' + ' 3\n' + ' 4'
    assert result == expected