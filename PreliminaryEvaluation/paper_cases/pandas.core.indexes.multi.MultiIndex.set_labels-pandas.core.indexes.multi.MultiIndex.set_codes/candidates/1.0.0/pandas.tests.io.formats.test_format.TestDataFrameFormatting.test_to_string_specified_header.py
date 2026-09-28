def test_to_string_specified_header(self):
    df = DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    df_s = df.to_string(header=['X', 'Y'])
    expected = '   X  Y\n0  1  4\n1  2  5\n2  3  6'
    assert df_s == expected
    with pytest.raises(ValueError):
        df.to_string(header=['X'])