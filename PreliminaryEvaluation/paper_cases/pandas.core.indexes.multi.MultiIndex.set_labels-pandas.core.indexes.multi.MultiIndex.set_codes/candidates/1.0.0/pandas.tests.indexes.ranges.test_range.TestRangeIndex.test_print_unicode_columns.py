def test_print_unicode_columns(self):
    df = pd.DataFrame({'א': [1, 2, 3], 'ב': [4, 5, 6], 'c': [7, 8, 9]})
    repr(df.columns)