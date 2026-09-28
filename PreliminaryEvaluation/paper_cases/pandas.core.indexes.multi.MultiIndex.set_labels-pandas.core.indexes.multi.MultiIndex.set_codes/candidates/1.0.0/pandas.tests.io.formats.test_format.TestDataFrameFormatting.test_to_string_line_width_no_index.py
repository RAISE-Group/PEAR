def test_to_string_line_width_no_index(self):
    df = DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    df_s = df.to_string(line_width=1, index=False)
    expected = ' x  \\\n 1   \n 2   \n 3   \n\n y  \n 4  \n 5  \n 6  '
    assert df_s == expected
    df = DataFrame({'x': [11, 22, 33], 'y': [4, 5, 6]})
    df_s = df.to_string(line_width=1, index=False)
    expected = '  x  \\\n 11   \n 22   \n 33   \n\n y  \n 4  \n 5  \n 6  '
    assert df_s == expected
    df = DataFrame({'x': [11, 22, -33], 'y': [4, 5, -6]})
    df_s = df.to_string(line_width=1, index=False)
    expected = '  x  \\\n 11   \n 22   \n-33   \n\n y  \n 4  \n 5  \n-6  '
    assert df_s == expected